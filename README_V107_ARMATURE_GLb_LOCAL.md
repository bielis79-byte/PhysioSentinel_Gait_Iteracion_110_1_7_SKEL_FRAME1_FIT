# V107 · modelo óseo pre-riggeado local

La pestaña 11 usa `PhysioSentinel_Skeleton_Rigged_v1.glb`, incluido dentro del despliegue. El modelo contiene nodos anatómicos explícitos: `Pelvis`, `Spine`, `Thorax`, `Neck`, `Head`, `Femur_L/R`, `Tibia_L/R`, `Foot_L/R`, `Humerus_L/R`, `Forearm_L/R` y `Hand_L/R`.

La cinemática procede del rig XYZ V104. V107 fuerza un ciclo visual determinista de 75 frames y aplica la pose de cada segmento directamente en cada frame, sin depender del frame anterior.

El objetivo de esta versión es validar el principio de retargeting sobre un modelo realmente jerarquizado antes de intentar transferir la misma estructura al atlas anatómico completo y, posteriormente, a la musculatura.

Modos disponibles: Rig, Esqueleto y Rig + Esqueleto. El visor permite reproducción, avance/retroceso frame a frame, slider, reencuadre y grabación/descarga del ciclo.
