# PhysioSentinel Gait · V106.3

- Corrige el bloqueo total de V106.2 al abrir la pestaña Atlas 3D.
- Causa: un salto de línea literal quedó dentro de una cadena JavaScript (`textContent += ...`) y provocaba un error de sintaxis antes de ejecutar incluso el rig fallback.
- El mensaje queda escapado como `\n`, por lo que el script puede parsearse y arrancar.
- Se conserva el import map único de V106.2 para `three`, `OrbitControls` y `GLTFLoader`.
- Se mantiene el rig V104 desacoplado, los 75 frames, armature pre-rigged, GPU SAFE y vídeo descargable.
- No se modifican métricas clínicas ni la trayectoria XYZ.
