# V105.3 · Hotfix de visibilidad

V105.2 cargaba correctamente las 201 mallas y los 75 frames, pero podía dejar la escena completamente fuera del frustum porque el atlas y el rig usaban escalas espaciales muy diferentes. V105.3 normaliza ambos sistemas antes del encuadre y ajusta los planos de clipping de la cámara.

Prueba recomendada: abrir `Rig`, después `Huesos`, después `Rig + Huesos`; usar `Reencuadrar` si se ha manipulado la cámara. Si los elementos se ven pero el hueso no sigue correctamente al rig, el problema restante es de registración/retargeting y no de carga o visibilidad.
