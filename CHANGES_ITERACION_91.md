# PhysioSentinel Gait V91

## Malla anatómica 3D real: motor de activo riggeado
- Se añade en la pestaña 11 un bloque V91 específico para mallas anatómicas GLB/glTF riggeadas.
- El motor distingue explícitamente entre el atlas procedimental heredado y una malla 3D real.
- Validación de GLB/glTF y manifiesto de retargeting auditable.
- Mapeo previsto de pelvis, columna, cabeza, brazos, antebrazos, muslos, piernas y pies a la cinemática 3D de PhysioSentinel.
- El skinning/pesos de vértices pertenecen al rig del activo anatómico cargado.
- Fuente cinemática preferente: reconstrucción biplanar frontal+lateral.
- La malla se considera anatomía genérica conducida por la cinemática de la paciente, no anatomía interna individual.
- Si no existe activo anatómico real, V91 lo declara de forma explícita y mantiene el atlas paramétrico como fallback, sin llamarlo malla real.

## Sin cambios
- V90 cinemática angular.
- HALPE26, tracking, IC/TO, métricas, Supabase y OpenCV/RTMLib/ONNX Runtime.
