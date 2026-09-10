# PhysioSentinel Gait V107.2

Hotfix de arranque OpenCV tras el ImportError observado en Streamlit Cloud en V107.1.

- Mantiene íntegro el modelo GLB pre-riggeado y el retargeting delta-rest de V107.1.
- Conserva la estrategia probada V86.6 con OpenCV 5.0.0.93 headless aislado.
- Valida primero la caché aislada existente.
- Si la caché está incompleta/corrupta, la elimina y reinstala con hasta 3 intentos, `--no-cache-dir` y timeout explícito.
- Si la instalación aislada no está disponible por un fallo transitorio de red/caché, usa como fallback el `cv2` del venv únicamente si contiene `VideoCapture`, `aruco` y `dnn`.
- El error final, si todos los caminos fallan, incluye la causa de cada intento para diagnóstico.
- No cambia métricas, detección, 3D V104, 75 frames, pivotes, GLB ni retargeting.
