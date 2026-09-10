# PhysioSentinel Gait · V108.3

## Mapa anatómico por identidad

- Mantiene el registro global y la cinemática de V108.2/V107.4 sin cambios.
- Sustituye la clasificación puramente espacial por una clasificación jerárquica:
  1. nombre/identidad de malla y nodo padre;
  2. metadata pública `mesh_mapping.json` de BodyExplorer cuando está disponible;
  3. fallback espacial conservador sólo cuando no existe identidad anatómica utilizable.
- Reglas anatómicas explícitas para fémur/rótula, tibia/peroné, huesos del pie, húmero, radio/cúbito, mano, pelvis/sacro, cráneo y esqueleto axial.
- Clavículas, escápulas, costillas, esternón y vértebras permanecen ligadas al tronco para evitar que la caja torácica sea capturada por controladores de brazo.
- El mapa se congela una sola vez en la pose de referencia; no hay reclasificación durante los 75 frames.
- El panel informa cuántas mallas fueron asignadas por IDENTIDAD/METADATA y cuántas necesitaron fallback ESPACIAL.
- Mantiene modo `Mapa binding` para auditoría visual.

V108.3 sigue siendo una etapa de validación del atlas real. No modifica métricas clínicas.
