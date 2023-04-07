# CafehuelenBackend
Backend para café huelen, servirá una api quien se encargará de hacer puente con la base de datos

# Te llevoAPP API<br>
API desarrollada con Django, Django REST framework y PostgreSQL, desplegada en [render.com](www.render.com) para servir preparaciones, ingredientes_preparaciones, ingredientes y categorias para [cafehuelen.cl](https://cafehuelen.cl) quién crea y administra preparaciones y manerjo de inventario mediante este servicio. 
## Para su futuro consumo se encontrará disponible en:<br> https://cafehuelen.cl/ <br><br>

# Características
Crear, leer (incluye detalle), actualizar y eliminar:
- Módulo de preparaciones:
    - preparaciones, ingredientes_preparaciones, ingredientes, categorias.
- Módulo de compras:
    - items de compra, compras y cupones
- Módulo de administración:  
    - totems, locales, supervisores de local y proveedores de local.

# Requerimientos
- asgiref==3.6.0
- Django==4.2
- djangorestframework==3.14.0
- pytz==2023.3
- sqlparse==0.4.3

Incluidos en requirements.txt para su fácil instalación.

# Imágenes
![Screenshot](https://raw.githubusercontent.com/keaguirre/djangoBackend/master/Screenshots/web.png)
