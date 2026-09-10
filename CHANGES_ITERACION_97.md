# PhysioSentinel Gait · Iteración 97.0

- Cargador GLB robusto: esqueleto y musculatura cargan de forma independiente.
- `raw.githubusercontent.com` es fuente primaria; jsDelivr queda como respaldo.
- Un fallo de musculatura ya no deja vacío el esqueleto, ni viceversa.
- El visor muestra estado y número de mallas cargadas para cada sistema.
- V97 intenta construir la cinemática 3D al abrir el atlas, sin exigir abrir antes V89/V60.
- Si falta el ciclo físico homólogo V48, crea un intervalo biplanar común sólo para retargeting visual.
- Ese rescate NO modifica V48-V52, IC/TO, métricas clínicas ni cinemática angular V90.
- Los GLB siguen siendo recursos externos y no se almacenan en Supabase.
