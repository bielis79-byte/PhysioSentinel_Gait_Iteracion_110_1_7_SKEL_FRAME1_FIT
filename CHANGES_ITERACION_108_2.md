# PhysioSentinel Gait · Iteración 108.2

- Mantiene el arranque JavaScript corregido de V108.1 y la cinemática V104/V107 de 75 frames.
- Sustituye el binding por proximidad al rig por un **registro global uniforme atlas→rig** y una **clasificación anatómica determinista** en la pose de referencia.
- El atlas se escala de forma uniforme a la altura del rig, se alinea por centro X/Z y por suelo Y.
- Las 201 mallas se asignan una sola vez a Pelvis, Trunk, Head, Humerus/Forearm/Hand L-R y Femur/Tibia/Foot L-R usando regiones relativas del atlas ya registrado.
- El mapa queda congelado durante los 75 frames; no hay reclasificación ni reparenting temporal.
- Nuevo modo **Mapa binding**: colorea las mallas por controlador para auditar visualmente la asociación.
- HUD con conteos por segmento y control de distribución para detectar asignaciones anómalas.
- No modifica métricas clínicas ni Supabase.
