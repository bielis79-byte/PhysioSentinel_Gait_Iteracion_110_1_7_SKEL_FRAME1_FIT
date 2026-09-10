# V106.1 · corrección de arranque JavaScript

La captura de V106 mostraba `Rig: OK` pero Three.js, GLTFLoader, Atlas y Armature en `pendiente`. La causa era determinista: la primera llamada a `apply(0)` accedía a `webglReady` antes de la declaración `let webglReady`, provocando un `ReferenceError` por Temporal Dead Zone.

V106.1 mueve la inicialización del estado WebGL antes de esa primera llamada. Si existe otro error del navegador, ahora se muestra en el panel de diagnóstico.
