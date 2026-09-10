# PhysioSentinel Gait V92 · OpenAtlas 3D verificable

## Cambio principal
V92 deja de tratar la incorporación de una malla real como un simple `file_uploader` GLB y crea un flujo auditable de activo anatómico + rig + licencia + retargeting.

- Nuevo bloque **V92 · OpenAtlas anatómico 3D · rigging/skinning + retargeting biplanar**.
- Preset de fuente abierta **Z-Anatomy / BodyParts3D** y opción para activo propio/licenciado.
- Carga de paquete ZIP anatómico con validación mínima obligatoria:
  - `model.glb` (o cualquier GLB dentro del paquete),
  - `rig_map.json`,
  - archivo `ATTRIBUTION`, `LICENSE` o `LICENCE`.
- Auditoría visible del paquete. V92 no ejecuta scripts embebidos dentro del ZIP.
- Exportación nueva de **retargeting JSON**: serializa, frame a frame, las articulaciones HALPE26 3D ya calculadas por PhysioSentinel para conducir un rig externo.
- El retargeting exporta fase 0–100 %, tiempo físico cuando existe y coordenadas X/Y/Z por landmark.
- Se mantiene el alias mapping de pelvis, columna, cabeza, brazos, antebrazos, muslos, piernas y pies.
- Preferencia cinemática: biplanar frontal+lateral; el modo monocular queda explícitamente marcado si se usa.

## Qué NO afirma V92
- No afirma que la malla sea la anatomía interna individual de la paciente.
- No convierte una imagen 2D en una malla 3D real.
- No redistribuye dentro del ZIP una malla anatómica de terceros sin revisar sus obligaciones de licencia/atribución.
- No sustituye la cinemática angular clínica de V90 por ángulos derivados del render visual.

## Fuente abierta preparada
El preset enlaza al repositorio oficial Z-Anatomy/Models-of-human-anatomy. El activo concreto que se use debe conservar sus atribuciones y condiciones de licencia. El objetivo de V92 es poder usar una exportación GLB riggeada/derivada de un atlas abierto sin ocultar el origen ni la licencia.

## Sin cambios
V90 cinemática angular; HALPE26; IC/TO; tracking; Supabase; OpenCV/RTMLib/ONNX Runtime; reconstrucción biplanar y exportaciones clínicas previas.
