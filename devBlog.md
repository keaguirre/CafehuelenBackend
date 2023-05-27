### Aqui un historial de los avances y dificultas del dia a dia del desarrollo

# 08/05/23
- Creadas las vistas con joins de nombres en vez de id's
- Creada la vista que permite busqueda de categoria mediante nombre

# 10/05/23
- [x] Las categorias desactivads, desactivarán las preparciones relacionadas y ambos no se listarán en las vistas principales.
- [x] Agregado el signals.py
- [/] Listado de categorías descartadas y mostrar con un collapse de daisyUI las preparaciones relacionadas.

# 11/05/23
- Vista nueva en el back, desactivados, nombre categoria, cuantas preparaciones, estado y un array con las preparaciones anidadas a esa categoria desactivada

# 14/05/23
- Estados añadidos a models y vistas en el bloque de local
- Modificada la vista de totem que buscaba detalle por num_totem en vez de mac.
- Añadido signals para que en la tabla de totem el num_totem sea incremental mediante este trigger.

# 15/05/23
- [x] Implementada la validacion de login desde el back.

# 17/05/23
- Creada nueva vista con preparaciones deshabilitadas y vista con actualización ('PATCH') para reactivar preparación.

# 26/05/23
- La automatización pasará a signals