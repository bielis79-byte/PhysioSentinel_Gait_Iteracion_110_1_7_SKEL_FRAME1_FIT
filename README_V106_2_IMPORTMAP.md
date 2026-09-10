# PhysioSentinel Gait V106.2

Hotfix de módulos ES para el visor 3D. La V106.1 demostró que el rig y el motor JavaScript arrancaban, pero OrbitControls/GLTFLoader fallaban al resolver el bare specifier `three`. V106.2 usa un import map versionado y un fallback esm.sh para que los tres módulos compartan la misma instancia de Three.js.

Secuencia esperada del panel:
1. Rig: OK
2. Three.js: OK
3. GLTFLoader + OrbitControls: OK
4. Atlas: GLB OK
5. Ligado armature: OK
6. Primer render WebGL: OK
