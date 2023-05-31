# {...} cafeScript API
API desarrollada con Django, Django REST framework y PostgreSQL, desplegada en [render.com](www.render.com) para servir preparaciones, ingredientes_preparaciones, ingredientes y categorias para [cafeScript.cl](https://cafeScript.cl) quién crea y administra preparaciones y manerjo de inventario mediante este servicio. 
## Para su futuro consumo se encontrará disponible en:<br> https://cafeScript.cl/ <br>

# Características
Crear, leer (incluye detalle), actualizar y eliminar:
- Módulo de preparaciones:
    - preparaciones, ingredientes_preparaciones, ingredientes, categorias.
- Módulo de compras:
    - items de compra, compras y cupones
- Módulo de administración:  
    - totems, locales, supervisores de local y proveedores de local.
- Para más información **http://localhost:8000/api/v1/docs**

# Requerimientos
- asgiref==3.6.0
- Django==4.2
- djangorestframework==3.14.0
- pytz==2023.3
- sqlparse==0.4.3

Incluidos en requirements.txt para su fácil instalación.

# Imágenes
## Home
![Home](https://raw.githubusercontent.com/keaguirre/cafeScript-Backend/main/Documentos/indexWeb.png)

## Home API 
![HomeAPI](https://raw.githubusercontent.com/keaguirre/cafeScript-Backend/main/Documentos/indexApi.png)
