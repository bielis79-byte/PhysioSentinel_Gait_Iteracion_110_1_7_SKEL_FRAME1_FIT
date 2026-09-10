# V103 · Validación XYZ antes del atlas

Objetivo: separar definitivamente tres problemas posibles: datos, reproductor y retargeting anatómico.

1. La app crea frames XYZ explícitos desde la reconstrucción 3D disponible.
2. El navegador recibe todos los frames una sola vez.
3. Los controles de reproducción funcionan localmente, sin modificar `st.session_state`.
4. El panel muestra coordenadas y desplazamientos numéricos entre el frame actual y el anterior.
5. El rig cian es el frame actual y el rig gris semitransparente es el anterior.
6. Sólo después de confirmar que esta secuencia camina de forma coherente se reactivará el atlas anatómico móvil.

El 3D estimado/no métrico continúa siendo una representación cinemática cualitativa cuando no existe calibración métrica válida.
