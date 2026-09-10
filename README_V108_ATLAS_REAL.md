# V108 · Atlas óseo anatómico real

V108 sustituye visualmente el esqueleto simplificado de validación por el `skeleton.glb` público de BodyExplorer, descrito por su repositorio como un atlas de 201 mallas óseas derivadas de BodyParts3D/Z-Anatomy.

La cinemática continúa procediendo del rig V104/V107 previamente validado. El atlas se registra al frame de referencia y cada malla queda ligada una sola vez al controlador segmentario más próximo. En los frames posteriores solo se aplican transformaciones delta respecto a reposo; no se vuelve a clasificar la anatomía y no hay acumulación temporal.

Esta iteración debe validarse visualmente en `Rig + Atlas`. El objetivo de V108 es comprobar que la transferencia del armature validado a la geometría anatómica real es estable. Una mala asignación de una pieza concreta debe corregirse en una tabla de binding determinista en la siguiente iteración, no mediante reparenting dinámico durante la marcha.

Fuente anatómica: Johan Bellander, BodyExplorer; BodyParts3D / Z-Anatomy. Consultar ATTRIBUTION_Z_ANATOMY_BODYParts3D.txt y las licencias de los datasets.
