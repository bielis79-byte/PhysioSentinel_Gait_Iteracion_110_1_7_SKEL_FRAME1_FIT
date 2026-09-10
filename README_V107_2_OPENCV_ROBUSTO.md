# V107.2 · OpenCV robusto

Esta revisión corrige únicamente el arranque de OpenCV observado en Streamlit Cloud. El motor anatómico V107.1 no se modifica.

Orden de carga de OpenCV:
1. caché headless V86.6 válida;
2. reinstalación aislada de `opencv-contrib-python-headless==5.0.0.93` con 3 intentos;
3. fallback al cv2 del entorno solo si expone las APIs requeridas.

No se añade `packages.txt` y no se desinstalan paquetes del venv.
