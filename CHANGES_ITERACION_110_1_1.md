# PhysioSentinel Gait · V110.1.1

## Hotfix de despliegue SKEL en Streamlit Cloud

- Corregido el fallo de instalación observado en V110.1.
- El log demuestra que `SKEL` completaba su metadata, pero la línea explícita de `MarilynKeller/chumpy` fallaba durante `build_wheel()` porque el entorno aislado de build no contenía `pip`.
- Eliminada la instalación explícita de `chumpy`; no forma parte del camino mínimo oficial actual de SKEL para el forward básico.
- SKEL queda fijado al commit que Streamlit resolvió correctamente en el despliegue fallido (`c32cf16581295bff19399379efe5b776d707cd95`) para reproducibilidad.
- Se mantienen PyTorch, `smplx`, `trimesh`, `tqdm` y `moderngl-window`.
- No se añade `packages.txt`.
- Los modelos privados `skel_male.pkl` / `skel_female.pkl` siguen siendo aportados por el usuario y no se redistribuyen.
- No se modifica la cinemática V104/V107 ni las métricas clínicas.
