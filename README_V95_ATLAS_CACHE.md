# V95 · política de almacenamiento del atlas

PhysioSentinel Gait V95 evita almacenar el atlas anatómico pesado en Supabase.

## Flujo
1. La aplicación comprueba la caché local/efímera de la instancia.
2. Si faltan `Z-Biomechanics.7z` o `Z-Anatomy.zip`, los descarga desde la fuente oficial.
3. Inspecciona ambos archivos y genera `atlas_manifest.json`.
4. Durante la vida de la instancia de Streamlit se reutiliza la misma copia.
5. Si la instancia se reinicia y la caché desaparece, los recursos se vuelven a descargar automáticamente.

## Supabase
Los binarios no se suben a Supabase Storage ni se duplican por paciente o sesión. La única información del atlas prevista para `gait_sessions` es:

`atlas_version = ZAnatomy_Gait_v1`

Para habilitarla, ejecutar una sola vez `SUPABASE_MIGRATION_V95.sql` en el SQL Editor de Supabase. Si no se ejecuta, la aplicación sigue guardando las sesiones; simplemente omite ese metadato.

## Alcance anatómico
Esta versión resuelve la política de adquisición/caché/almacenamiento. No convierte por sí sola el atlas Blender original en una malla final skinneada; la validación de armature/pesos sigue siendo obligatoria antes de declarar una animación anatómica deformable real.
