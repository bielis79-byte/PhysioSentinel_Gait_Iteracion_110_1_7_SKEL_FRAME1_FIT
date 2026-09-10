# Iteración 106.2

- Corrige el error de V106.1 `Failed to resolve module specifier "three"`.
- Añade un `importmap` único para Three.js 0.180.0 y `three/addons/`.
- Three.js, OrbitControls y GLTFLoader se resuelven desde el mismo árbol de módulos.
- Añade fallback vía esm.sh si el import map/CDN primario falla.
- Mantiene el rig V104 independiente del atlas, 75 frames, armature pre-rigged, GPU SAFE y grabación descargable.
- Huesos y Rig + Huesos sólo se habilitan tras carga de GLB, ligado del armature y primer render.
