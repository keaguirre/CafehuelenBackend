from django.urls import path, include
from .views import actualizacion_stock, categoria_list, categoria_detail, cat_find_id, ingrediente_list, ingrediente_detail, detalle_prep_list, detalle_prep_detail, preparacion_disabled_update, preparacion_list, preparacion_detail, get_disabled_catList, preparacion_disabled_list

urlpatterns = [   
    path('categorias/', categoria_list),
    path('categorias/<int:id_cat>', categoria_detail),
    path('categorias/find_id/<str:nombre_cat>', cat_find_id),
    path('categorias/deshabilitadas', get_disabled_catList),
    path('ingredientes/', ingrediente_list),
    path('ingredientes/<int:id_ingre>',ingrediente_detail),
    path('ingredientes/stock/<int:id_ingre>',actualizacion_stock),
    path('detalles_prep/', detalle_prep_list),
    path('detalles_prep/<int:id_detalle_prep>', detalle_prep_detail),
    path('preparaciones/', preparacion_list),
    path('preparaciones/<int:id_prep>', preparacion_detail),
    path('preparaciones/deshabilitadas', preparacion_disabled_list),
    path('preparaciones/deshabilitadas/<int:id_prep>', preparacion_disabled_update),
#-------------------------------------------
]