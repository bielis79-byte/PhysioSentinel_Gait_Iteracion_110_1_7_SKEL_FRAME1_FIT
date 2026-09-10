# PhysioSentinel Gait · V105.6

- El Rig V104 queda desacoplado de la carga del atlas y aparece inmediatamente mediante canvas 2D de respaldo.
- La carga 3D se divide en estados verificables: Three.js, GLTFLoader, GLB óseo y primer render WebGL.
- Huesos y Rig + Huesos permanecen desactivados hasta completar un primer render del atlas.
- Se añaden timeout, fuentes CDN alternativas y botón `Reintentar atlas`.
- Un fallo del atlas ya no bloquea el Rig, el scrubber, la reproducción ni la grabación del Rig.
- Se conserva el retargeting V105.4 y la descarga de vídeo introducida en V105.5.
