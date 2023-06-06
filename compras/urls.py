from django.urls import path, include
from .views import  compra_list, compra_detail, compras_por_mes_anual, item_compra_list, item_compra_detail, item_compra_auto, compras_recientes, compras_recientes_paginadas, compras_dia_semana, total_compras_mes, total_compras_mes_anterior_x_semana, total_compras_mes_x_semana, total_compras_semana_anual
urlpatterns = [   
    path('compras/', compra_list),
    path('compras/<int:id_compra>',compra_detail),
    path('compras/compras_recientes', compras_recientes),
    path('compras/compras_recientes_paginadas', compras_recientes_paginadas),
    path('items_compra/', item_compra_list),
    path('items_compra/<int:id_item_compra>', item_compra_detail),
    path('items_compra_auto/', item_compra_auto),
    #-----------Analiticas--------------------------------
    path('analiticas/cantidad_compras/compras_dia_semana/', compras_dia_semana),
    path('analiticas/cantidad_compras/total_compras_mes/', total_compras_mes),
    path('analiticas/cantidad_compras/total_compras_mes_x_semana/', total_compras_mes_x_semana),
    path('analiticas/cantidad_compras/total_compras_mes_anterior_x_semana/', total_compras_mes_anterior_x_semana),
    path('analiticas/cantidad_compras/compras_por_mes_anual/', compras_por_mes_anual),
    path('analiticas/cantidad_compras/total_compras_semana_anual/', total_compras_semana_anual),
]