# V109 — SKEL Proof-of-Concept

- Nueva rama experimental SKEL; V108.3 queda conservada para comparación.
- Mantiene V104/V107 como fuente cinemática y no cambia métricas clínicas.
- Primer objetivo deliberadamente limitado: frame 1 -> landmarks objetivo -> preparación de fit SKEL.
- Exporta `V109_SKEL_target_frame_001.csv`.
- Acepta un ZIP privado de modelos SKEL únicamente para auditar disponibilidad; no lo persiste ni lo envía a Supabase.
- No incluye ni redistribuye código/modelos SKEL.
- Incluye `V109_SKEL_LOCAL_RUNNER.py` para comprobar un forward pass SKEL en un entorno local autorizado.
- No se afirma todavía que exista ajuste de los 46 q de SKEL: esa optimización es la siguiente etapa una vez validado el runtime/modelo.
- Rama marcada como investigación/no comercial por las condiciones de licencia estándar de SKEL.
