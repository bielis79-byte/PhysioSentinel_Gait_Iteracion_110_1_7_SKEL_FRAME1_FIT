# PhysioSentinel Gait · Iteración 88

## Avatar musculoesquelético de superficie animado

- Sustituye el render anatómico V87 por un atlas visual paramétrico de superficie más detallado.
- Esqueleto: fémur con cabeza/cuello/condilos aproximados, tibia/peroné y radio/cúbito separados, articulaciones, pelvis, columna, parrilla costal, cráneo y pie.
- Musculatura visual: grupos diferenciados de cuádriceps, isquiotibiales/aductores, glúteos, tibial anterior, gemelos/sóleo, deltoides, bíceps/tríceps, antebrazo y tronco.
- La geometría se recalcula en cada fotograma usando las coordenadas 3D estimadas del paciente; no es una fotografía estática.
- Vídeo 3D principal, multivista y reproyección 2D se muestran con autoplay y loop en la pestaña 11.
- Se conserva la selección Esqueleto técnico / Esqueleto anatómico / Modelo musculoesquelético.
- No modifica HALPE26, tracking, métricas biomecánicas, reconstrucción 3D, Supabase ni RTMLib/ONNXRuntime.

## Alcance

El modelo es anatomía genérica paramétrica con finalidad de visualización. No es un atlas anatómico segmentado del paciente, no estima activación muscular, fuerza, EMG ni volumen muscular real.
