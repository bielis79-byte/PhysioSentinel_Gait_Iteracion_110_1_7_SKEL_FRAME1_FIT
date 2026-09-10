# PhysioSentinel Gait · Iteración 107.3

## Objetivo
Corregir la falta de coincidencia espacial observada en V107.1 entre el rig V104 y el GLB simplificado, antes de transferir el sistema a las 201 mallas anatómicas del atlas.

## Cambios
- Registro articular determinista: cada segmento se coloca desde su articulación proximal hacia la distal en cada frame.
- Calibración longitudinal por segmento (fémur, tibia, pie, húmero, antebrazo, columna y cuello) usando la distancia V104 del propio frame.
- Pelvis y tórax reciben bases rígidas 3D construidas con ambas caderas/hombros y el eje del tronco.
- Los 17 controladores conocidos del GLB se conectan una sola vez a la raíz del modelo. No hay clasificación espacial ni reparenting por frame.
- No existe acumulación temporal: cada frame depende exclusivamente de las coordenadas V104 de ese frame.
- Puntos de validación magenta colocados exactamente en las articulaciones del rig para comprobar superposición.
- Material óseo `MeshBasicMaterial` claro para garantizar visibilidad incluso con variaciones de iluminación/WebGL.
- Se conserva el modo GPU seguro y la grabación del ciclo.

## Criterio de aprobación
En `Rig + Esqueleto`, los pivotes de cadera, rodilla, tobillo, hombro, codo y muñeca deben mantenerse superpuestos al rig V104 durante los 75 frames. Esta versión sigue usando el GLB segmentario propio; no es todavía `skeleton.glb` de BodyExplorer/Z-Anatomy.
