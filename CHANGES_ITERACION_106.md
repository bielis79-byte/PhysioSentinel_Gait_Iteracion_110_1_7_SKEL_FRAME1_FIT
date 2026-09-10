# PhysioSentinel Gait · Iteración 106

## Cambio de arquitectura

V106 abandona el retargeting por re-clasificación/reparentado durante cada frame. El atlas óseo se carga una sola vez y sus 201 mallas se ligan a un armature segmentario persistente.

## Armature

- Segmentos: muslo, pierna, pie, brazo y antebrazo izquierdos/derechos, más bloque axial.
- Cada grupo usa un pivote de referencia anatómico aproximado calculado en el espacio del atlas.
- El ligado se realiza una sola vez al cargar el GLB.
- Durante la reproducción sólo se actualizan posición y quaternion de cada nodo desde la secuencia XYZ V104.
- No hay transformaciones acumulativas entre frames.

## Interfaz

- Modos Rig, Huesos y Rig + Huesos.
- Rig independiente de la carga del atlas.
- Estados visibles: Three.js, GLTFLoader, atlas, ligado del armature y primer render.
- Reintento del atlas.
- Reproducción, ±1 frame, slider, reset y reencuadre.
- Grabación descargable del modo visible.

## Alcance

El armature V106 es una capa visual experimental. No modifica IC/TO, segmentación, métricas ni interpretación clínica.
