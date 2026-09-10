# PhysioSentinel Gait · Iteración 90

## Objetivo
Integrar el análisis cinemático angular en la pestaña del ciclo de marcha sin duplicar la segmentación temporal existente y corregir la denominación del atlas anatómico para no sobreprometer realismo.

## Cambios
- APP_VERSION = 90.0.
- La pestaña 9 pasa a llamarse `9 · Ciclo + Cinemática angular`.
- Se mantiene V52 IC→TO→IC y se añade V90 sobre el mismo ciclo físico normalizado 0–100 %.
- Plano sagital: curvas de cadera, rodilla y tobillo cuando la vista lateral las hace evaluables.
- Resumen por articulación/lado: mínimo, máximo, ROM y media.
- Tabla por fase con valor del paciente y rango de referencia.
- Referencias de fase sagital: tabla de población sana GaitON, PMCID PMC11870036.
- Rodilla: conversión explícita del ángulo interno publicado a flexión clínica (0°≈extensión).
- Tobillo: conserva la convención angular geométrica de PhysioSentinel para evitar mezclar convenciones.
- La banda continua mostrada es una interpolación visual entre intervalos publicados por fase; no se presenta como curva normativa instrumental continua.
- Plano frontal/posterior: curvas descriptivas disponibles del mismo ciclo, sin imponer bandas normativas no transferibles.
- Plano transverso: se mantiene como estimación limitada; no se etiqueta la rotación axial verdadera de cadera/rodilla como medición 3D instrumentada.
- Exportación nueva `10_cinematica_angular_v90/` con curvas 0–100 %, comparación por fase, resumen ROM/min/max y LEEME metodológico.
- La capa `Atlas anatómico realista · experimental` se renombra a `Atlas anatómico paramétrico · experimental`.
- Se añade aviso explícito: para un acabado tipo atlas profesional hace falta una malla 3D externa con licencia compatible y rigging/skinning. V90 no redistribuye una malla anatómica de terceros sin licencia.
- No se alteran HALPE26, tracking, eventos V47–V52, Supabase, OpenCV/RTMLib/ONNX Runtime ni la reconstrucción biplanar existente.

## Nota clínica
Las referencias por fase son descriptivas y no sustituyen un laboratorio 3D optoelectrónico, plataforma de fuerzas ni evaluación clínica. La cinemática 2D/biplanar conserva las limitaciones de perspectiva, marcadores virtuales y modelo geométrico.
