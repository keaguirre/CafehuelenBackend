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

## To do:
- [x] Agregar el campo estado a las demas tablas en el modulo Compra y Local
