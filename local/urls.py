from django.urls import path, include
from .views import cupon_list, cupon_detail, compra_list, compra_detail, item_compra_list, item_compra_detail
urlpatterns = [   #corregir al bloque correspondiente
    path('cupon/', cupon_list),
    path('cupon/<str:nombre_cup>', cupon_detail),
    path('compra/', compra_list),
    path('compra/<int:id_compra>',compra_detail),
    path('item_compra/', item_compra_list),
    path('item_compra/<int:id_prep>', item_compra_detail),
]