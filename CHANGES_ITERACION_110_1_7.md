# PhysioSentinel Gait · Iteración 110.1.7

## SKEL · ajuste real del primer frame

- Parte de V110.1.6, que ya valida runtime SKEL + modelo privado + forward CPU real.
- Mantiene congeladas las fuentes cinemáticas V104/V107 y NO procesa todavía los 75 frames.
- Resuelve las correspondencias a partir de `model.joints_name`, sin fijar índices SKEL a ciegas.
- Ajusta un único frame mediante los joints anatómicos SKEL compatibles con los landmarks XYZ.
- Optimiza los 46 parámetros de pose de SKEL y una orientación global 3D; estima escala isotrópica y traslación global para registrar el sistema XYZ V104/V107.
- Mantiene `betas=0` en esta puerta de validación para no confundir pose con identidad/forma corporal.
- Ejecuta fitting en CPU con `skelmesh=False`; el modelo privado permanece exclusivamente en `/tmp`.
- Añade RMSE antes/después, porcentaje de mejora, auditoría por articulación y superposición 3D XYZ objetivo vs SKEL.
- Añade exportación JSON del ajuste del frame 1 (`pose_46`, transformación global y correspondencias).
- No modifica NumPy, Pose2Sim, OpenSim, métricas clínicas ni la rama V104/V107.
- BodyExplorer/Z-Anatomy continúan fuera del flujo activo.

## Criterio de avance

Sólo si la superposición del frame 1 es anatómicamente coherente se extenderá el ajuste a frames 2→75 con continuidad temporal para construir la animación de marcha.
