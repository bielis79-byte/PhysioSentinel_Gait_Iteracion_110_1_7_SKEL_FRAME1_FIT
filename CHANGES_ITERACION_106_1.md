# PhysioSentinel Gait V106.1

- Corrige un bloqueo JavaScript de V106: `apply(0)` consultaba `webglReady` antes de que la variable fuese inicializada (`let` / Temporal Dead Zone).
- El rig podía dibujarse porque `drawFallback()` se ejecutaba antes del acceso inválido, pero después el script se detenía y Three.js/GLTFLoader/Atlas quedaban permanentemente en `pendiente`.
- Las variables del motor 3D se inicializan ahora antes de la primera llamada a `apply(0)`.
- Añadidos diagnósticos visibles para `window.error` y `unhandledrejection`.
- No cambia la cinemática V104, el armature, la clasificación ósea ni las métricas clínicas.
