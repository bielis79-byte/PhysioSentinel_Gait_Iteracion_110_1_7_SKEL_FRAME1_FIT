# PhysioSentinel Gait · Iteración 107.4

## Objetivo
Validar cuantitativamente el registro articular de V107.3 antes de pasar al atlas anatómico real.

## Cambios
- No cambia la cinemática de V107.3.
- En modo **Rig + Esqueleto** muestra simultáneamente el rig V104 (cian), los pivotes reales del GLB (magenta) y una línea roja entre cada par.
- Calcula por frame el error de 12 articulaciones: caderas, rodillas, tobillos, hombros, codos y muñecas.
- Informa RMS y error máximo en unidades del visor y como porcentaje de la altura corporal mapeada.
- El vídeo descargable conserva estas ayudas visuales de validación.
- Sigue siendo un modelo GLB simplificado propio; todavía no incorpora las 201 mallas del skeleton.glb de BodyExplorer/Z-Anatomy.
