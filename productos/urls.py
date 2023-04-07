from django.urls import path, include
from .views import categoria_list, categoria_detail, ingrediente_list, ingrediente_detail, ingrediente_prep_list, ingrediente_prep_detail, preparacion_list, preparacion_detail
urlpatterns = [   
    path('categoria/', categoria_list),
    path('categoria/<str:nombre_cat>', categoria_detail),
    path('ingrediente/', ingrediente_list),
    path('ingrediente/<int:id_ingre>',ingrediente_detail),
    path('ingrediente_prep/', ingrediente_prep_list),
    path('ingrediente_prep/<int:id_prep>', ingrediente_prep_detail),
    path('preparacion/', preparacion_list),
    path('preparacion/<int:id_prep>', preparacion_detail),
]