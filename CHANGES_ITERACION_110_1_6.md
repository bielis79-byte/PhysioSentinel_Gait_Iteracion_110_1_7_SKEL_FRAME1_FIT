# PhysioSentinel Gait · V110.1.6

Hotfix acumulativo SKEL CPU + primer forward real de 1 frame.

- Parte de V110.1.5 y conserva intacta la fuente cinemática V104/V107.
- Corrige imports omitidos en el hotfix temporal (`tempfile` y `Path`).
- SKEL se instala en `/tmp/physiosentinel_skel_cpu_v110_1_6` con `pip --no-deps --target`; no escribe en `/home/adminuser/venv/.../site-packages`.
- Mantiene NumPy 2.x y no instala `moderngl-window`.
- Extrae únicamente `skel_male.pkl` o `skel_female.pkl` del ZIP privado a `/tmp/physiosentinel_skel_models_v110_1_6`.
- Usa la API del commit fijado: `SKEL(gender=..., model_path=<directorio>)`.
- Ejecuta en CPU un forward real de batch 1 con `pose=(1,46)`, `betas=(1,10)` y `trans=(1,3)`.
- Informa vértices de piel, vértices de esqueleto y salida articular cuando el forward finaliza.
- No procesa aún los 75 frames ni hace fitting XYZ: primero debe superarse esta puerta de validación.
- BodyExplorer/Z-Anatomy sigue fuera del flujo activo.
