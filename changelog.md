# Changelog
Aquí irá el registro de cambios y commits con su fecha y descripción.

# 06/04/23 App API Productos
- Creacion de app de productos, la cual involucra las tablas: Preparacion, Ingredientes_preparacion, Ingrediente, Categoria
- Añadida la carpeta de documentos con los diagramas de base de datos y de zonas
- Creada la app core la cual contiene la pagina de home

# 07/04/23 App API Compras
- Creacion de app de compras, la cual involucra las tablas: Cupon, Compra, Item_compra
- Creada la App API Local 

# 07/04/23 App API Local
- Creacion de app de local, la cual involucra las tablas: Local, Totem, Supervisores_local, Proveedor
- Cambio de imagen de preview del sitio

# 09/04/23 Cambios de ruta
- Se cambia de lugar el home de la api desde home a /api
- Se cambia el home por el home under construction

# 21/04/23 Actualizacion de categorias
- Vuelve a ocuparse el id en la tabla de categorias
- Ajustes menores en settings.py, zona horaria, lenguage
- Nueva base de datos aplicada
- Corregido el metodo put

# 24/04/23 Correcciones en el view
- Se corrige el view de producto que creaba ingredientes por error en el serializer
- Quitamos el campo cant unidad desde ingreprep por innecesario
- Regeneramos la base de datos

# 27/04/23 Correccion de models
- Entra id_cat_prep por nombre_cat_prep
- Se corrigen los models para que on_delete=CASCADE pasa a ser on_delete=SET_DEFAULT en los 3 bloques

# 28/04/23 Paso a prod en Render.com
- Agregado, build.sh, Actualizados settings.py y requirements

# 29/04/23 Refactor en models categorias
- Agregado el metodo para que la tabla categoria detecte las entradas repetidas y deja un nuevo mensaje.

# 03/05/23 Refactor del modelo de base de datos
- Agregado el campo estado a todas las tablas como boolean, será el nuevo delete
- Cambio nombre de ingre_prep a detalle_preparacion
- Cambiados los nombres de las tablas a todo minuscula y corregidas todas las menciones
- Drop tabla cupon y proveedor
- Cambio en ingrediente, descripcion_ingrediente por nombre_ingrediente
- Actualizado el /api para que las redirecciones concordaran con los nuevos nombres

### 03/05/23 RollBack minusculas en nombres de tablas
- RollBack Cambiados los nombres de las tablas a todo minuscula y corregidas todas las menciones debido a errores mayores, se prefiere hacer rollback a ese detalle antes que rehacer todos los metodos en views denuevo.
- Creado el metodo PATCH para cada view.

# 08/05/23
- Creadas las vistas con joins de nombres en vez de id's
- Creada la vista que permite busqueda de categoria mediante nombre

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
- Alterada la tabla de totem, pk numtomtem, creada la vista busqueda totem por mac.
- Alterada la tabla de item_compra quien no tenia id.

# 22/05/23
- Correccion del detalle de item_compra.
- Correccion de view en item_compra, apuntaba el modelo equivocado en el metodo post.

# 25/05/23
- Quitado el totem de modulo local y las referencias a el en otros modulos
- Provisoriamente se esta ocupando sqlite3 para los cambios mientras que se terminan ajustes en el front.

# 26/05/23
- Agregado default=True en los estados en todos los modelos
- Corrido el login a http://localhost:8000/api/superv_local/[usuario]
- automatizacion de descuento de cantidad por receta ingredientes, item_compra_auto en bloque compras **En desarrollo**
- Implementación de CoreAPI Docs en http://localhost:8000/api/docs

# 29/05/23
- Agregado el parametro v1 despues de api para versionar la api.
- Creada la vista compras recientes en el módulo de compras, la cual tiene, numero_compra, tipo_servicio y [ compras relacionadas ]
- Rebranding hecho

# 30/05/23
- [x]automatizacion de descuento de cantidad por receta ingredientes, item_compra_auto en bloque compras **Completado**
- nueva vista para agregar el stock

# 03/06/23
- Creada la vista de compras recientes con paginacion en http://localhost:8000/api/v1/compras/compras_recientes_paginadas y si se quiere solicitar por alguna pagina se usa el parametro ?page=[numero de la pagina] al final de la url

# 06/06/23
- Creadas las vistas de analiticas de compras en el bloque de compras.
- Se crea un nuevo item en el index api para ir a la pagina de analiticas.
- Analiticas de cantidad de compras.
- Analiticas de total monetario de compras.

# 16/06/23
- Cuando no hay stock en items compra auto, resuelve un 200, en vez de un 500 y devuelve un msj de que no hay stock
- Agregado estado compra a compras recientes paginadas
- Detalle compra arreglado.
- Agregado PATCH a detalle compra para actualizar los pedidos

# 19/06/23
- Terminada la automatizacion retorna el listado de preparaciones que no tienen stock.

## To do:
- [ ] Modificar la automatización para que cuando uno de las preparaciones ordenadas no tenga stock de ingredientes, devolver un no hay stock<br>si se puede, que retorne cual es la que no tiene stock para que el usuario pueda ordenar nuevamente sin volver a ordenar la que no tiene stock.