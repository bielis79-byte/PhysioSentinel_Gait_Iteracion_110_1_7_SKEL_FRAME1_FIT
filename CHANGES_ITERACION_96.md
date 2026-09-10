# PhysioSentinel Gait V96

V96 añade un visor Three.js con geometría GLB anatómica real de huesos y músculos derivada de Z-Anatomy/BodyParts3D (BodyExplorer). Lee los frames 3D de PhysioSentinel y aplica retargeting visual segmentario a las estructuras anatómicas. Los GLB se cargan externamente en el navegador y no se suben a Supabase.

La geometría es real de atlas, pero genérica. El movimiento V96 es retargeting rígido segmentario; no se etiqueta como skinning continuo porque estos GLB no se validan como armature + vertex weights compatibles con el rig de PhysioSentinel.
