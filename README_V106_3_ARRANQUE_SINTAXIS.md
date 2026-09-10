# V106.3 · Arranque sintáctico corregido

V106.2 no ejecutaba el módulo JavaScript porque una cadena de diagnóstico contenía un salto de línea literal. Esto impedía que apareciera incluso el rig, dejando todos los estados en pendiente. V106.3 corrige esa cadena y conserva el import map estable.
