# V108.2 — Registro global y binding anatómico determinista

V108.2 corrige el problema observado en V108.1: el atlas cargaba correctamente, pero la asignación por distancia hacía que decenas de mallas terminaran en un mismo antebrazo/húmero.

La nueva estrategia separa tres capas: (1) movimiento V104/V107 ya validado, (2) registro global del atlas real al sistema corporal del rig, y (3) mapa de 201 mallas a controladores anatómicos calculado una sola vez en reposo.

El modo `Mapa binding` permite auditar esa tercera capa antes de considerar definitivo el atlas. La anatomía real sigue siendo BodyExplorer / BodyParts3D / Z-Anatomy y conserva sus atribuciones y licencias de origen.
