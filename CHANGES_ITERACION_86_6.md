# PhysioSentinel Gait · Iteración 86.6

## Hotfix estructural OpenCV 5 + RTMLib 0.0.16 / ONNX Runtime

La V86.5 confirmó en Streamlit Cloud que las ruedas OpenCV 4.12.0.88 y 4.11.0.86 fallan durante la propia importación de `cv2` por incompatibilidades internas de `cv2.typing` (`cv2.dnn.DictValue`). Por ello V86.6 abandona la cadena de downgrade 4.x.

### Cambios

- Se restaura `opencv-contrib-python-headless==5.0.0.93` en un target aislado de `/tmp`, estrategia que en V86.2 ya permitió arrancar la aplicación y llegar al análisis.
- Se evita importar las ruedas GUI (`opencv-python` / `opencv-contrib-python`) instaladas transitivamente por Pose2Sim.
- Se añade un shim mínimo de compatibilidad para RTMLib 0.0.16: solo si faltan, expone en `cv2.dnn` los símbolos clásicos `DNN_BACKEND_OPENCV`, `DNN_TARGET_CPU`, `DNN_BACKEND_CUDA` y `DNN_TARGET_CUDA` que RTMLib consulta al construir `RTMLIB_SETTINGS` durante el import.
- La inferencia de pose continúa forzada a `backend = "onnxruntime"`; por tanto esos símbolos de compatibilidad no se emplean para ejecutar la red neuronal y no emulan OpenCV-DNN.
- Se mantienen intactos HALPE26, tracking, análisis biomecánico, Supabase, reconstrucción 2D/3D, vídeos y avatar anatómico V86.
- `APP_VERSION` actualizado a `86.6`.
- Sin `packages.txt` y sin modificación/desinstalación del entorno gestionado por Streamlit.

## Motivo técnico

RTMLib 0.0.16 construye su tabla de backends al importarse y referencia constantes DNN clásicas incluso cuando el backend solicitado es ONNX Runtime. OpenCV 5 cambia esa API, pero PhysioSentinel no necesita OpenCV-DNN para la inferencia porque utiliza ONNX Runtime. V86.6 desacopla ambas cosas: OpenCV 5 headless para vídeo/visión y ONNX Runtime para RTMPose.
