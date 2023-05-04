from django.urls import path, include
from .views import categoria_list, categoria_detail, ingrediente_list, ingrediente_detail, detalle_prep_list, detalle_prep_detail, preparacion_list, preparacion_detail
urlpatterns = [   
    path('categoria/', categoria_list),
    path('categoria/<int:id_cat>', categoria_detail),
    path('ingrediente/', ingrediente_list),
    path('ingrediente/<int:id_ingre>',ingrediente_detail),
    path('detalle_prep/', detalle_prep_list),
    path('detalle_prep/<int:id_detalle_prep>', detalle_prep_detail),
    path('preparacion/', preparacion_list),
    path('preparacion/<int:id_prep>', preparacion_detail),
]