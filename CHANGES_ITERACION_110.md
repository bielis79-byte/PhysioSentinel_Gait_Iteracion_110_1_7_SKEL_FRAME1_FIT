# PhysioSentinel Gait V110 — SKEL ajuste anatómico de un frame

- Se congela el puente V104/V107 validado en V109.1: 75 frames y 15 landmarks objetivo.
- V110 NO anima todavía: usa un único frame como puerta de validación.
- Añade normalización pélvica y métricas geométricas del objetivo (altura XYZ, anchura pélvica, longitudes segmentarias).
- Añade control de preparación SKEL y auditoría del ZIP privado del modelo.
- Si el runtime `skel` y el modelo privado están disponibles, la interfaz queda habilitada para el forward/fitting; si no, informa exactamente qué dependencia falta y no fabrica una malla sustituta.
- Criterio para pasar a V111: ajuste articular de un frame validado antes de extender a 75 frames.
- Sin cambios en métricas clínicas, Supabase, detección IC/TO ni cinemática V104/V107.
