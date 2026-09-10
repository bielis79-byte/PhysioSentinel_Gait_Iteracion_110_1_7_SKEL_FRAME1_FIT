# PhysioSentinel Gait · Iteración 95

## Objetivo
Separar completamente los activos anatómicos pesados del almacenamiento clínico de Supabase.

## Cambios V95
- `APP_VERSION = 95.0`.
- Atlas lógico: `ZAnatomy_Gait_v1`.
- `Z-Anatomy.zip` y `Z-Biomechanics.7z` se tratan como **recursos externos/locales de ejecución**.
- Descarga automática desde la fuente oficial cuando el recurso no existe en la instancia.
- Caché temporal de ejecución bajo el directorio temporal de Streamlit; mientras la instancia siga viva los archivos se reutilizan.
- Si Streamlit Cloud reinicia la instancia y elimina la caché efímera, V95 vuelve a descargar/preparar automáticamente los activos.
- Auditoría del contenido antes de declararlo disponible.
- Supabase no recibe los ~103 MB de atlas. Únicamente puede guardar `atlas_version = ZAnatomy_Gait_v1` en `gait_sessions`.
- La escritura de `atlas_version` es *best effort*: si todavía no se ha aplicado la migración SQL, el guardado de la sesión clínica continúa sin fallar.
- Se incluye `SUPABASE_MIGRATION_V95.sql` para añadir el campo opcional.

## Regla de validez mantenida
Descargar Z-Anatomy/Z-Biomechanics no equivale por sí mismo a disponer de una malla deformable. PhysioSentinel solo debe denominar el resultado como rigging/skinning real cuando el activo final conserve armature y pesos de vértices.
