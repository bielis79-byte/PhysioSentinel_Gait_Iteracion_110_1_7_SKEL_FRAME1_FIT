# PhysioSentinel Gait V109 — SKEL Proof-of-Concept

Objetivo: dejar de adaptar un atlas estático y probar un modelo esquelético paramétrico animable.

V109 NO incluye SKEL ni sus modelos. El usuario debe obtenerlos personalmente del portal oficial y aceptar su licencia. La licencia estándar publicada por SKEL permite investigación científica/educación no comercial y prohíbe la incorporación a un producto/servicio comercial sin licencia comercial.

## Fase V109
1. Conserva el ciclo V104/V107 de 75 frames.
2. Extrae el frame 1 como objetivo articular explícito.
3. Permite auditar un ZIP privado con `skel_male.pkl`/`skel_female.pkl` sin persistirlo.
4. Incluye runner local para comprobar el forward pass de SKEL en un entorno autorizado.
5. No finge un fit: convertir HALPE26/XYZ a los 46 q requiere optimización/retargeting y se implementará solo tras comprobar que el modelo puede ejecutarse legal y técnicamente.

Fuentes oficiales: skel.is.tue.mpg.de y github.com/MarilynKeller/SKEL.
