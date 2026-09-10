from __future__ import annotations
import io, json, zipfile, re, sys, subprocess, importlib, tempfile, os
from pathlib import Path
import numpy as np
import pandas as pd
import streamlit as st

# Landmarks mínimos que ya están presentes en la secuencia V104/V107 y son útiles
# para el ajuste articular inicial de SKEL.
JOINTS = [
    "LHip","RHip","LKnee","RKnee","LAnkle","RAnkle",
    "LShoulder","RShoulder","LElbow","RElbow","LWrist","RWrist",
    "Neck","Head","Hip"
]

# Alias tolerantes para no depender de una única convención de nombres.
_ALIASES = {
    "lhip": "LHip", "lefthip": "LHip", "left_hip": "LHip", "hipleft": "LHip",
    "rhip": "RHip", "righthip": "RHip", "right_hip": "RHip", "hipright": "RHip",
    "lknee": "LKnee", "leftknee": "LKnee", "left_knee": "LKnee", "kneeleft": "LKnee",
    "rknee": "RKnee", "rightknee": "RKnee", "right_knee": "RKnee", "kneeright": "RKnee",
    "lankle": "LAnkle", "leftankle": "LAnkle", "left_ankle": "LAnkle", "ankleleft": "LAnkle",
    "rankle": "RAnkle", "rightankle": "RAnkle", "right_ankle": "RAnkle", "ankleright": "RAnkle",
    "lshoulder": "LShoulder", "leftshoulder": "LShoulder", "left_shoulder": "LShoulder",
    "rshoulder": "RShoulder", "rightshoulder": "RShoulder", "right_shoulder": "RShoulder",
    "lelbow": "LElbow", "leftelbow": "LElbow", "left_elbow": "LElbow",
    "relbow": "RElbow", "rightelbow": "RElbow", "right_elbow": "RElbow",
    "lwrist": "LWrist", "leftwrist": "LWrist", "left_wrist": "LWrist",
    "rwrist": "RWrist", "rightwrist": "RWrist", "right_wrist": "RWrist",
    "neck": "Neck", "head": "Head", "nose": "Nose", "hip": "Hip",
}

def _norm_name(name: str) -> str:
    s = str(name).strip()
    compact = re.sub(r"[^a-z0-9]", "", s.lower())
    # Primero coincidencia exacta canónica.
    for canon in JOINTS + ["Nose"]:
        if compact == re.sub(r"[^a-z0-9]", "", canon.lower()):
            return canon
    # Después alias con y sin separadores.
    raw = s.lower().replace("-", "_").replace(" ", "_")
    return _ALIASES.get(raw, _ALIASES.get(compact, s))

def _xyz(v):
    try:
        if isinstance(v, dict):
            # Aceptar X/Y/Z y x/y/z.
            keys = {str(k).lower(): k for k in v.keys()}
            if all(k in keys for k in ("x","y","z")):
                a = [v[keys["x"]], v[keys["y"]], v[keys["z"]]]
            else:
                return None
        elif isinstance(v, (list, tuple, np.ndarray, pd.Series)) and len(v) >= 3:
            a = [v[0], v[1], v[2]]
        else:
            return None
        a = [float(x) for x in a]
        return a if np.isfinite(a).all() else None
    except Exception:
        return None

def _frame_points_from_frame(f):
    if not isinstance(f, dict):
        return {}
    # V104/V107 oficial usa `joints`; se mantienen los otros nombres como compatibilidad.
    src = f.get("joints")
    if not isinstance(src, dict) or not src:
        src = f.get("points")
    if not isinstance(src, dict) or not src:
        src = f.get("landmarks")
    if not isinstance(src, dict):
        return {}
    out = {}
    for k, v in src.items():
        p = _xyz(v)
        if p is not None:
            out[_norm_name(k)] = p

    # Centros derivados sólo para visualización/registro inicial. No sustituyen landmarks medidos.
    if "Hip" not in out and "LHip" in out and "RHip" in out:
        out["Hip"] = ((np.asarray(out["LHip"]) + np.asarray(out["RHip"])) / 2.0).tolist()
    if "Neck" not in out and "LShoulder" in out and "RShoulder" in out:
        out["Neck"] = ((np.asarray(out["LShoulder"]) + np.asarray(out["RShoulder"])) / 2.0).tolist()
    if "Head" not in out and "Nose" in out:
        out["Head"] = list(out["Nose"])
    return out

def _select_best_frame(motion):
    frames = list((motion or {}).get("frames") or [])
    best_i, best_pts, best_score = 0, {}, -1
    for i, f in enumerate(frames):
        pts = _frame_points_from_frame(f)
        score = sum(1 for j in JOINTS if j in pts)
        if score > best_score:
            best_i, best_pts, best_score = i, pts, score
        # 14+ ya es un frame excelente para este PoC; evitamos recorrer de más.
        if score >= 14:
            break
    return best_i, best_pts, max(0, best_score)

def _target_csv(points, frame_index=0):
    rows = []
    for j in JOINTS:
        if j in points:
            x, y, z = points[j]
            rows.append({"frame": int(frame_index)+1, "joint": j, "x": x, "y": y, "z": z,
                         "source": "derived" if j in ("Hip",) else "V104/V107"})
    return pd.DataFrame(rows)

def _inspect_private_bundle(data: bytes):
    info={"has_male":False,"has_female":False,"files":[],"valid_zip":False}
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            names=z.namelist(); info["valid_zip"]=True
            info["files"]=names[:80]
            low=[n.lower() for n in names]
            info["has_male"]=any(n.endswith("skel_male.pkl") for n in low)
            info["has_female"]=any(n.endswith("skel_female.pkl") for n in low)
    except Exception as e:
        info["error"]=str(e)
    return info

def _plot_frame(df):
    if df.empty:
        return
    try:
        import plotly.graph_objects as go
        links = [
            ("LShoulder","RShoulder"),("LShoulder","LElbow"),("LElbow","LWrist"),
            ("RShoulder","RElbow"),("RElbow","RWrist"),("LShoulder","LHip"),
            ("RShoulder","RHip"),("LHip","RHip"),("LHip","LKnee"),("LKnee","LAnkle"),
            ("RHip","RKnee"),("RKnee","RAnkle"),("Neck","LShoulder"),("Neck","RShoulder"),("Neck","Head")
        ]
        P={r.joint:(r.x,r.y,r.z) for r in df.itertuples()}
        fig=go.Figure()
        for a,b in links:
            if a in P and b in P:
                xa,ya,za=P[a]; xb,yb,zb=P[b]
                fig.add_trace(go.Scatter3d(x=[xa,xb],y=[ya,yb],z=[za,zb],mode="lines",showlegend=False,hoverinfo="skip"))
        fig.add_trace(go.Scatter3d(x=df.x,y=df.y,z=df.z,mode="markers+text",text=df.joint,
                                   textposition="top center",name="Landmarks objetivo"))
        fig.update_layout(height=520,margin=dict(l=0,r=0,t=35,b=0),title="Frame objetivo V110.1.3 · XYZ para ajuste SKEL",
                          scene=dict(aspectmode="data"))
        st.plotly_chart(fig,use_container_width=True)
    except Exception as exc:
        st.caption(f"Visualización 3D no disponible: {exc}")



# V110.1.7 · correspondencia anatómica entre landmarks V104/V107 y joints SKEL.
# Se resuelve por nombre real del modelo (`model.joints_name`), evitando índices rígidos.
_SKEL_TARGET_CANDIDATES = {
    "Hip": ["pelvis"],
    "RHip": ["femur_r", "hip_r", "rhip"],
    "RKnee": ["tibia_r", "knee_r", "rknee"],
    "RAnkle": ["talus_r", "ankle_r", "rankle"],
    "LHip": ["femur_l", "hip_l", "lhip"],
    "LKnee": ["tibia_l", "knee_l", "lknee"],
    "LAnkle": ["talus_l", "ankle_l", "lankle"],
    "RShoulder": ["humerus_r", "shoulder_r", "rshoulder"],
    "RElbow": ["ulna_r", "elbow_r", "relbow"],
    "RWrist": ["hand_r", "wrist_r", "rwrist"],
    "LShoulder": ["humerus_l", "shoulder_l", "lshoulder"],
    "LElbow": ["ulna_l", "elbow_l", "lelbow"],
    "LWrist": ["hand_l", "wrist_l", "lwrist"],
    "Head": ["head", "skull"],
}

def _simple_name(v):
    if isinstance(v, bytes):
        try: v=v.decode("utf-8")
        except Exception: v=str(v)
    return re.sub(r"[^a-z0-9]", "", str(v).lower())

def _resolve_skel_correspondence(model, target_df):
    raw_names=getattr(model,"joints_name",[])
    names=list(raw_names) if raw_names is not None else []
    norm={_simple_name(n):i for i,n in enumerate(names)}
    rows=[]
    for target_name,cands in _SKEL_TARGET_CANDIDATES.items():
        if target_name not in set(target_df["joint"].astype(str)):
            continue
        found=None
        for cand in cands:
            key=_simple_name(cand)
            if key in norm:
                found=norm[key]; break
        if found is not None:
            rows.append((target_name,int(found),str(names[found])))
    return rows, names

def _rodrigues_torch(torch, r):
    # Rotación 3D diferenciable desde vector axis-angle.
    theta=torch.sqrt(torch.sum(r*r)+1e-12)
    k=r/theta
    K=torch.stack([
        torch.stack([torch.zeros_like(k[0]),-k[2],k[1]]),
        torch.stack([k[2],torch.zeros_like(k[0]),-k[0]]),
        torch.stack([-k[1],k[0],torch.zeros_like(k[0])])
    ])
    I=torch.eye(3,dtype=r.dtype,device=r.device)
    return I + torch.sin(theta)*K + (1.0-torch.cos(theta))*(K@K)

def _similarity_to_target(torch, src, tgt, rotvec):
    # src/tgt: Nx3. Rotación libre + escala isotrópica + traslación analítica.
    R=_rodrigues_torch(torch,rotvec)
    src_mean=src.mean(dim=0,keepdim=True)
    tgt_mean=tgt.mean(dim=0,keepdim=True)
    src_c=src-src_mean
    tgt_c=tgt-tgt_mean
    src_r=src_c @ R.T
    src_rms=torch.sqrt(torch.mean(torch.sum(src_r*src_r,dim=1))+1e-12)
    tgt_rms=torch.sqrt(torch.mean(torch.sum(tgt_c*tgt_c,dim=1))+1e-12)
    scale=tgt_rms/src_rms
    pred=src_r*scale+tgt_mean
    trans=tgt_mean.squeeze(0)-scale*(src_mean.squeeze(0) @ R.T)
    return pred,R,scale,trans

def _plot_skel_fit(target_df, fit_rows, before_xyz, after_xyz, all_after=None, all_names=None):
    try:
        import plotly.graph_objects as go
        target_map={r.joint:np.array([r.x,r.y,r.z],float) for r in target_df.itertuples()}
        names=[r[0] for r in fit_rows]
        T=np.stack([target_map[n] for n in names])
        fig=go.Figure()
        fig.add_trace(go.Scatter3d(x=T[:,0],y=T[:,1],z=T[:,2],mode="markers+text",text=names,textposition="top center",name="XYZ objetivo"))
        fig.add_trace(go.Scatter3d(x=before_xyz[:,0],y=before_xyz[:,1],z=before_xyz[:,2],mode="markers",name="SKEL antes"))
        fig.add_trace(go.Scatter3d(x=after_xyz[:,0],y=after_xyz[:,1],z=after_xyz[:,2],mode="markers+text",text=names,textposition="bottom center",name="SKEL ajustado"))
        for i,n in enumerate(names):
            fig.add_trace(go.Scatter3d(x=[T[i,0],after_xyz[i,0]],y=[T[i,1],after_xyz[i,1]],z=[T[i,2],after_xyz[i,2]],mode="lines",showlegend=False,hoverinfo="skip"))
        fig.update_layout(height=620,margin=dict(l=0,r=0,t=45,b=0),title="V110.1.7 · XYZ objetivo vs SKEL antes/después del ajuste",scene=dict(aspectmode="data"))
        st.plotly_chart(fig,use_container_width=True)
    except Exception as exc:
        st.caption(f"Visualización del fit no disponible: {exc}")

def _fit_one_skel_frame(torch, model, target_df, max_iter=45):
    rows, joint_names=_resolve_skel_correspondence(model,target_df)
    if len(rows)<8:
        raise RuntimeError(f"Sólo se pudieron resolver {len(rows)} correspondencias SKEL↔XYZ; se requieren al menos 8. joints_name={joint_names}")
    target_map={r.joint:np.array([r.x,r.y,r.z],np.float32) for r in target_df.itertuples()}
    tgt_np=np.stack([target_map[r[0]] for r in rows]).astype(np.float32)
    idx=torch.tensor([r[1] for r in rows],dtype=torch.long,device="cpu")
    tgt=torch.tensor(tgt_np,dtype=torch.float32,device="cpu")
    betas=torch.zeros((1,int(model.num_betas)),dtype=torch.float32,device="cpu")
    zero_trans=torch.zeros((1,3),dtype=torch.float32,device="cpu")

    # Primero registramos la T-pose con una orientación global libre.
    pose=torch.zeros((1,int(model.num_q_params)),dtype=torch.float32,device="cpu",requires_grad=True)
    rotvec=torch.zeros((3,),dtype=torch.float32,device="cpu",requires_grad=True)
    opt=torch.optim.Adam([pose,rotvec],lr=0.035)
    history=[]
    before_model=None
    for it in range(int(max_iter)):
        opt.zero_grad(set_to_none=True)
        out=model(pose,betas,zero_trans,skelmesh=False)
        J=out.joints[0]
        sel=J.index_select(0,idx)
        if before_model is None:
            before_model=sel.detach().clone()
        pred,R,scale,trans=_similarity_to_target(torch,sel,tgt,rotvec)
        data_loss=torch.mean(torch.sum((pred-tgt)**2,dim=1))
        # Regularización suave: evita soluciones articulares extremas en una sola imagen.
        pose_reg=1.0e-4*torch.mean(pose*pose)
        loss=data_loss+pose_reg
        loss.backward()
        torch.nn.utils.clip_grad_norm_([pose,rotvec],10.0)
        opt.step()
        with torch.no_grad():
            pose.clamp_(-3.14159,3.14159)
            rotvec.clamp_(-3.14159,3.14159)
        history.append(float(data_loss.detach().cpu()))

    with torch.no_grad():
        out=model(pose,betas,zero_trans,skelmesh=False)
        J=out.joints[0]
        sel=J.index_select(0,idx)
        pred,R,scale,trans=_similarity_to_target(torch,sel,tgt,rotvec)
        # T-pose inicial bajo su mejor registro global, para comparar justamente pose vs pose.
        Rf=R.detach(); sf=scale.detach(); tf=trans.detach()
        before_all=(before_model @ Rf.T)*sf + tf
        after_all=(J @ Rf.T)*sf + tf
        before=before_all.detach().cpu().numpy()
        after=pred.detach().cpu().numpy()
        tgt_arr=tgt.detach().cpu().numpy()
        err_before=np.linalg.norm(before-tgt_arr,axis=1)
        err_after=np.linalg.norm(after-tgt_arr,axis=1)
        return {
            "rows":rows,"joint_names":joint_names,"pose":pose.detach().cpu().numpy()[0],
            "rotvec":rotvec.detach().cpu().numpy(),"scale":float(sf.cpu()),"trans":tf.cpu().numpy(),
            "target":tgt_arr,"before":before,"after":after,"all_after":after_all.detach().cpu().numpy(),
            "rmse_before":float(np.sqrt(np.mean(err_before**2))),"rmse_after":float(np.sqrt(np.mean(err_after**2))),
            "errors_before":err_before,"errors_after":err_after,"history":history,
        }

def render_skel_poc_panel(motion):
    frames=list((motion or {}).get("frames") or [])
    if not frames:
        st.warning("No hay secuencia V104/V107 disponible para construir el frame objetivo de SKEL.")
        return

    best_i, pts, score = _select_best_frame(motion)
    df = _target_csv(pts, best_i)
    raw_count = len(_frame_points_from_frame(frames[best_i])) if frames else 0

    st.success(f"Motor cinemático disponible: {len(frames)} frames. V110 usa el primer frame con cobertura articular suficiente como puerta de validación antes de animar SKEL.")
    c1,c2,c3,c4=st.columns(4)
    c1.metric("Frames V104/V107",len(frames))
    c2.metric("Landmarks objetivo",len(df))
    c3.metric("Frame seleccionado",f"{best_i+1}/{len(frames)}")
    c4.metric("SKEL","entrada XYZ")

    if len(df) == 0:
        st.error("V109.1 sigue sin encontrar landmarks compatibles dentro del payload V104/V107.")
        st.write("Claves presentes en el frame seleccionado:", list((frames[best_i].get("joints") or {}).keys())[:40])
        return
    elif len(df) < 10:
        st.warning(f"Sólo se han recuperado {len(df)} landmarks objetivo. El CSV es utilizable para diagnóstico, pero todavía no para un ajuste SKEL fiable.")
    else:
        st.info(f"Puente V104/V107 → SKEL recuperado: {len(df)} landmarks objetivo de {raw_count} puntos XYZ disponibles en el frame {best_i+1}.")

    st.download_button("⬇️ Frame objetivo V110 (CSV)",df.to_csv(index=False).encode("utf-8-sig"),
                       "V110_1_2_SKEL_target_frame.csv","text/csv",use_container_width=True)
    st.caption("Este CSV contiene las coordenadas XYZ que se usarán para el ajuste articular. Los centros derivados están identificados y no modifican ninguna métrica clínica.")

    _plot_frame(df)
    with st.expander("Ver coordenadas XYZ del frame objetivo", expanded=False):
        st.dataframe(df, use_container_width=True, hide_index=True)

    # Diagnóstico geométrico previo al fitting: no altera datos ni métricas clínicas.
    P={r.joint:np.array([r.x,r.y,r.z],dtype=float) for r in df.itertuples()}
    def dist(a,b):
        return float(np.linalg.norm(P[a]-P[b])) if a in P and b in P else float("nan")
    segs={
        "Pelvis L-R":dist("LHip","RHip"),
        "Fémur L":dist("LHip","LKnee"), "Fémur R":dist("RHip","RKnee"),
        "Tibia L":dist("LKnee","LAnkle"), "Tibia R":dist("RKnee","RAnkle"),
        "Húmero L":dist("LShoulder","LElbow"), "Húmero R":dist("RShoulder","RElbow"),
        "Antebrazo L":dist("LElbow","LWrist"), "Antebrazo R":dist("RElbow","RWrist"),
    }
    arr=df[["x","y","z"]].to_numpy(float)
    span=np.nanmax(arr,axis=0)-np.nanmin(arr,axis=0)
    st.markdown("**Control geométrico previo al fit**")
    q1,q2,q3=st.columns(3)
    q1.metric("Landmarks válidos",len(df))
    q2.metric("Extensión XYZ máx.",f"{float(np.max(span)):.3f}")
    finite=[v for v in segs.values() if np.isfinite(v) and v>0]
    q3.metric("Segmentos evaluables",len(finite))
    with st.expander("Longitudes del frame objetivo",expanded=False):
        st.dataframe(pd.DataFrame([{"segmento":k,"longitud_unidades_XYZ":v} for k,v in segs.items()]),use_container_width=True,hide_index=True)

    st.markdown("**Modelo SKEL privado · runtime V110.1.7 CPU + ajuste frame 1**")
    st.caption("El puente XYZ ya está validado. Para que V110 genere y ajuste la malla esquelética SKEL real debes aportar tu ZIP oficial con `skel_male.pkl` o `skel_female.pkl`.")
    bundle=st.file_uploader("ZIP privado con los archivos de modelo SKEL descargados por ti desde el portal oficial",type=["zip"],key="v110_1_skel_private_bundle",help="No se guarda en Supabase ni se incorpora a la exportación de PhysioSentinel.")
    if bundle is None:
        st.info("Entrada articular preparada: 15 landmarks. Falta únicamente el modelo SKEL privado para ejecutar el ajuste anatómico real de este frame. V110 no sustituye SKEL por una malla falsa.")
        return
    raw=bundle.getvalue(); audit=_inspect_private_bundle(raw)
    if not audit.get("valid_zip"):
        st.error("El archivo aportado no es un ZIP SKEL válido."); return
    st.write({"skel_male.pkl":audit["has_male"],"skel_female.pkl":audit["has_female"]})
    if not (audit["has_male"] or audit["has_female"]):
        st.error("No encuentro skel_male.pkl ni skel_female.pkl en el ZIP. No se ejecuta ningún modelo."); return
    # V110.1.6: runtime SKEL CPU aislado + modelo privado extraído sólo a /tmp.
    # No se toca el venv administrado, NumPy, OpenSim ni el stack gráfico ModernGL.
    def _import_or_install_skel_cpu():
        try:
            import torch as _torch
            from skel.skel_model import SKEL as _SKEL  # type: ignore
            return _torch, _SKEL, None
        except Exception as first_exc:
            try:
                # Streamlit Cloud no permite escribir de forma fiable en el site-packages
                # del venv durante la ejecución. Instalamos SKEL en un target temporal
                # escribible, igual que el aislamiento probado de OpenCV V86.6.
                url = "git+https://github.com/MarilynKeller/SKEL.git@c32cf16581295bff19399379efe5b776d707cd95"
                target = Path(tempfile.gettempdir()) / "physiosentinel_skel_cpu_v110_1_7"
                marker = target / ".ready"
                target.mkdir(parents=True, exist_ok=True)
                if str(target) not in sys.path:
                    sys.path.insert(0, str(target))
                if not marker.exists():
                    cmd = [sys.executable, "-m", "pip", "install", "--no-deps",
                           "--disable-pip-version-check", "--no-cache-dir",
                           "--target", str(target), url]
                    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
                    if proc.returncode != 0:
                        tail = (proc.stderr or proc.stdout or "")[-4000:]
                        return None, None, f"Instalación SKEL aislada falló ({proc.returncode}):\n{tail}"
                    marker.write_text("ok", encoding="utf-8")
                importlib.invalidate_caches()
                # Evita conservar un import parcial fallido anterior al instalar.
                for name in list(sys.modules):
                    if name == "skel" or name.startswith("skel."):
                        sys.modules.pop(name, None)
                import torch as _torch
                from skel.skel_model import SKEL as _SKEL  # type: ignore
                return _torch, _SKEL, None
            except Exception as second_exc:
                return None, None, f"Import inicial: {type(first_exc).__name__}: {first_exc}\nInstalación/import CPU: {type(second_exc).__name__}: {second_exc}"

    with st.spinner("Preparando runtime SKEL CPU aislado (sin ModernGL)…"):
        torch, SKEL, runtime_error = _import_or_install_skel_cpu()
    runtime = torch is not None and SKEL is not None
    if not runtime:
        st.error("El bundle privado es válido, pero el runtime SKEL CPU no ha podido prepararse. V110.1.7 evita deliberadamente moderngl-window para mantener NumPy 2.x compatible con Pose2Sim/OpenSim.")
        st.code(runtime_error or "Error de importación no especificado")
    else:
        st.success(f"Runtime SKEL REAL detectado · PyTorch {torch.__version__} · modelo privado presente · modo CPU sin ModernGL.")

        # Extraer exclusivamente el PKL elegido a un directorio temporal escribible.
        genders=[]
        if audit.get("has_male"): genders.append("male")
        if audit.get("has_female"): genders.append("female")
        gender=st.selectbox("Modelo SKEL para la prueba de 1 frame",genders,index=0,key="v110_1_7_gender")
        model_name=f"skel_{gender}.pkl"
        model_root=Path(tempfile.gettempdir()) / "physiosentinel_skel_models_v110_1_7"
        model_root.mkdir(parents=True,exist_ok=True)
        model_path=model_root / model_name
        try:
            with zipfile.ZipFile(io.BytesIO(raw)) as z:
                matches=[n for n in z.namelist() if n.lower().endswith(model_name)]
                if not matches:
                    raise FileNotFoundError(model_name)
                with z.open(matches[0]) as src, open(model_path,"wb") as dst:
                    dst.write(src.read())
        except Exception as exc:
            st.error(f"No se pudo extraer {model_name} al runtime temporal: {type(exc).__name__}: {exc}")
            return

        def _build_skel_model():
            # El commit fijado y versiones posteriores han usado ambas convenciones:
            # model_path explícito o SKEL_MODEL_PATH/directorio por defecto. Probamos
            # de forma controlada sin escribir fuera de /tmp.
            errs=[]
            try:
                # En el commit c32cf165..., `model_path` debe ser el DIRECTORIO;
                # SKEL concatena internamente skel_<gender>.pkl.
                return SKEL(gender=gender, model_path=str(model_root)), "model_path=/tmp/.../", None
            except Exception as exc:
                errs.append(f"model_path=dir: {type(exc).__name__}: {exc}")
                return None, None, "\n".join(errs)

        with st.spinner("Instanciando SKEL y ejecutando el primer forward CPU (1 frame)…"):
            model, init_mode, init_error = _build_skel_model()
            if model is None:
                st.error("SKEL se importa correctamente, pero no ha podido abrir el modelo privado desde /tmp.")
                st.code(init_error or "Error de inicialización no especificado")
                return
            try:
                model=model.to("cpu")
                pose=torch.zeros((1,int(model.num_q_params)),dtype=torch.float32,device="cpu")
                betas=torch.zeros((1,int(model.num_betas)),dtype=torch.float32,device="cpu")
                trans=torch.zeros((1,3),dtype=torch.float32,device="cpu")
                with torch.no_grad():
                    out=model(pose,betas,trans)
                skin=getattr(out,"skin_verts",None)
                skelv=getattr(out,"skel_verts",None)
                joints=getattr(out,"joints",None)
                if joints is None:
                    joints=getattr(out,"joints_ori",None)
                st.success("✅ Primer forward SKEL REAL completado en CPU para 1 frame.")
                f1,f2,f3,f4=st.columns(4)
                f1.metric("q / pose",int(model.num_q_params))
                f2.metric("betas",int(model.num_betas))
                f3.metric("skin verts",int(skin.shape[-2]) if skin is not None else "—")
                f4.metric("skel verts",int(skelv.shape[-2]) if skelv is not None else "—")
                st.caption(f"Inicialización: {init_mode} · modelo privado: {model_name} · almacenamiento temporal: /tmp · batch=1 · CPU")
                if joints is not None:
                    st.caption(f"Salida articular SKEL: shape {tuple(joints.shape)}")
                st.info("Puerta de runtime superada. V110.1.7 continúa ahora con el ajuste anatómico del frame 1; todavía NO procesa los 75 frames.")

                st.markdown("### V110.1.7 · Ajuste SKEL ↔ XYZ del frame 1")
                st.caption("Se optimiza la pose SKEL sobre sus joints anatómicos y se estima una transformación global rígida + escala isotrópica para registrar el sistema de coordenadas V104/V107. Betas permanecen neutras en esta puerta de validación.")
                try:
                    with st.spinner("Ajustando pose SKEL al frame XYZ (CPU, una sola vez)…"):
                        fit=_fit_one_skel_frame(torch,model,df,max_iter=45)
                    nfit=len(fit["rows"])
                    a1,a2,a3,a4=st.columns(4)
                    a1.metric("Correspondencias",f"{nfit}")
                    a2.metric("RMSE antes",f"{fit['rmse_before']:.4f}")
                    a3.metric("RMSE después",f"{fit['rmse_after']:.4f}")
                    improve=(1.0-fit['rmse_after']/max(fit['rmse_before'],1e-12))*100.0
                    a4.metric("Mejora",f"{improve:.1f} %")
                    if np.isfinite(improve) and improve>20:
                        st.success("✅ Ajuste del frame 1 completado: SKEL responde a la pose objetivo y reduce el error articular.")
                    else:
                        st.warning("El forward es válido, pero el primer ajuste todavía no reduce suficientemente el error. No se extenderá a 75 frames hasta revisar correspondencias/orientación.")
                    _plot_skel_fit(df,fit["rows"],fit["before"],fit["after"],fit.get("all_after"),fit.get("joint_names"))
                    erows=[]
                    for i,(target_name,jidx,skel_name) in enumerate(fit["rows"]):
                        erows.append({"XYZ objetivo":target_name,"SKEL joint":skel_name,"índice SKEL":jidx,"error antes":float(fit['errors_before'][i]),"error después":float(fit['errors_after'][i])})
                    with st.expander("Auditoría de correspondencias y error articular",expanded=False):
                        st.dataframe(pd.DataFrame(erows),use_container_width=True,hide_index=True)
                        st.write({"escala_global":fit["scale"],"traslacion_global":fit["trans"].tolist(),"rotacion_axis_angle":fit["rotvec"].tolist()})
                    export={
                        "version":"110.1.7","frame":int(best_i)+1,"gender":gender,"rmse_before":fit["rmse_before"],"rmse_after":fit["rmse_after"],
                        "scale":fit["scale"],"translation":fit["trans"].tolist(),"global_rotation_axis_angle":fit["rotvec"].tolist(),
                        "pose_46":fit["pose"].tolist(),
                        "correspondences":[{"target":r[0],"skel_index":int(r[1]),"skel_joint":r[2]} for r in fit["rows"]]
                    }
                    st.download_button("⬇️ Descargar ajuste SKEL frame 1 (JSON)",json.dumps(export,ensure_ascii=False,indent=2).encode("utf-8"),"V110_1_7_SKEL_fit_frame1.json","application/json",use_container_width=True)
                    st.info("Si esta superposición es anatómicamente correcta, el siguiente paso será reutilizar esta identidad/registro como inicialización temporal y resolver frames 2→75 con continuidad, que es la puerta hacia la marcha animada.")
                except Exception as fit_exc:
                    st.error("SKEL funciona, pero V110.1.7 no ha podido completar el ajuste del frame 1.")
                    st.code(f"{type(fit_exc).__name__}: {fit_exc}")
            except Exception as exc:
                st.error("El modelo SKEL se ha instanciado, pero el primer forward CPU ha fallado.")
                st.code(f"{type(exc).__name__}: {exc}")
                return
