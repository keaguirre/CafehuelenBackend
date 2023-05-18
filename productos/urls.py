from django.urls import path, include
from .views import categoria_list, categoria_detail, cat_find_id, ingrediente_list, ingrediente_detail, detalle_prep_list, detalle_prep_detail, preparacion_disabled_update, preparacion_list, preparacion_detail, get_disabled_catList, preparacion_disabled_list

urlpatterns = [   
    path('categoria/', categoria_list),
    path('categoria/<int:id_cat>', categoria_detail),
    path('categoria/find_id/<str:nombre_cat>', cat_find_id),
    path('categoria/deshabilitadas', get_disabled_catList),
    path('ingrediente/', ingrediente_list),
    path('ingrediente/<int:id_ingre>',ingrediente_detail),
    path('detalle_prep/', detalle_prep_list),
    path('detalle_prep/<int:id_detalle_prep>', detalle_prep_detail),
    path('preparacion/', preparacion_list),
    path('preparacion/<int:id_prep>', preparacion_detail),
    path('preparacion/deshabilitadas', preparacion_disabled_list),
    path('preparacion/deshabilitadas/<int:id_prep>', preparacion_disabled_update),
#-------------------------------------------
]