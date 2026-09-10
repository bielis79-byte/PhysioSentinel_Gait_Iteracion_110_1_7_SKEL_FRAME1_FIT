# PhysioSentinel Gait · Iteración 98

## Objetivo
Corregir el visor anatómico real de V97 cuando las 201 mallas óseas y 467 musculares cargaban correctamente pero permanecían fuera de cámara o invisibles.

## Cambios
- Autoencuadre determinista mediante `THREE.Box3` sobre las geometrías originales.
- Separación `atlasFrame` / `atlasContent`: la traslación al centro ocurre dentro del nodo escalado y evita la inconsistencia de V97.
- Normalización automática de escala a un volumen visible estable.
- Ajuste dinámico de cámara, `near`, `far`, `OrbitControls` y objetivo.
- Pose estática como estado inicial obligatorio; la animación no comienza hasta pulsar `Reproducir`.
- Diagnóstico visible: mallas, tamaño XYZ normalizado, centro, escala, distancia de cámara y clipping.
- Botón `Reencuadrar`.
- Huesos / Músculos / Ambos recalculan el encuadre según la capa visible.
- `frustumCulled=False` y materiales `DoubleSide` como defensa frente a mallas anatómicas con orientación/culling problemáticos.
- Se conservan intactos HALPE26, análisis biomecánico, V48–V52, V90, Supabase y la cinemática biplanar de V97.

## Limitación vigente
La animación continúa siendo retargeting segmentario sobre mallas anatómicas reales. Todavía no es skinning continuo con armature/pesos de vértice.
