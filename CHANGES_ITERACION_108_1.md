# V108.1 — Arranque JavaScript corregido

- Corrige un error sintáctico real de V108 en `segmentFrames()`: una llave cerraba el bucle antes de `return out`, provocando `SyntaxError: Illegal return statement`.
- Ese error explica exactamente que toda la interfaz quedara en `Rig: iniciando / Three.js: pendiente / GLTFLoader: pendiente`.
- No modifica la cinemática V104/V107, el ciclo de 75 frames ni el algoritmo de binding del atlas.
- Mantiene `skeleton.glb` BodyExplorer (201 mallas) con GitHub Raw + jsDelivr fallback.
- Validación de entrega: Python compila y el módulo JavaScript generado pasa `node --check`.
