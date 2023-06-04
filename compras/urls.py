from django.urls import path, include
from .views import  compra_list, compra_detail, item_compra_list, item_compra_detail, item_compra_auto, compras_recientes, compras_recientes_paginadas
urlpatterns = [   
    path('compras/', compra_list),
    path('compras/<int:id_compra>',compra_detail),
    path('compras/compras_recientes', compras_recientes),
    path('compras/compras_recientes_paginadas', compras_recientes_paginadas),
    path('items_compra/', item_compra_list),
    path('items_compra/<int:id_item_compra>', item_compra_detail),
    path('items_compra_auto/', item_compra_auto),
]