# V108.3 · Atlas óseo real con binding por identidad

Objetivo: corregir las asignaciones anatómicamente implausibles observadas en V108.2 sin tocar el motor cinemático validado.

El `skeleton.glb` de BodyExplorer contiene 201 mallas óseas. V108.3 intenta identificar cada malla usando primero su nombre, su nodo padre y la metadata pública de BodyExplorer (`mesh_mapping.json`). Cuando esos datos no permiten reconocer el hueso, se utiliza un fallback espacial más conservador.

El resultado debe auditarse con `Mapa binding`: las estructuras axiales deben conservar un color de tronco/pelvis/cabeza y las extremidades deben mostrar agrupaciones laterales coherentes. El contador `Identidad/metadata` permite saber cuánto del atlas pudo resolverse por identidad real frente a inferencia espacial.
