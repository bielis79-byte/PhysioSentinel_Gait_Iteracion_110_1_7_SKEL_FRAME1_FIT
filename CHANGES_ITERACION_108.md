# PhysioSentinel Gait · Iteración 108

- Integra por primera vez el `skeleton.glb` anatómico real de BodyExplorer (201 mallas óseas) como geometría animada.
- Mantiene sin cambios la secuencia V104/V107 validada de 75 frames.
- El atlas se descarga en el navegador desde GitHub Raw, con jsDelivr como respaldo; no se guarda en Supabase.
- Registro inicial global del atlas al cuerpo del rig y binding segmentario calculado una sola vez en el frame de referencia.
- Cada malla anatómica conserva su matriz de reposo y, durante la reproducción, recibe `M_actual_segmento * inverse(M_reposo_segmento) * M_reposo_malla`.
- No existe acumulación entre frames.
- Modo Rig / Atlas real / Rig + Atlas, reencuadre y grabación de ciclo.
- V108 es una fase de integración anatómica: todavía hay que validar que la asignación de cada una de las 201 superficies óseas a su segmento sea anatómicamente correcta antes de considerarlo definitivo.
