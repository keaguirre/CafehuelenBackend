from django.urls import path, include
from .views import  cantidad_compras_hoy, compra_list, compra_detail, compras_por_mes_anual, item_compra_list, item_compra_detail, item_compra_auto, compras_recientes, compras_recientes_paginadas, compras_dia_semana, sum_total_compra_week, total_compra_diaria_semanal, total_compra_semanal_anual, total_compra_semanal_mes, total_compra_semanal_mes_anterior, total_compras_hoy, total_compras_mes, total_compras_mes_anterior_x_semana, total_compras_mes_x_semana, total_compras_por_mes_anual, total_compras_semana_anual
urlpatterns = [   
    path('compras/', compra_list),
    path('compras/<int:id_compra>',compra_detail),
    path('compras/compras_recientes', compras_recientes),
    path('compras/compras_recientes_paginadas', compras_recientes_paginadas),
    path('items_compra/', item_compra_list),
    path('items_compra/<int:id_item_compra>', item_compra_detail),
    path('items_compra_auto/', item_compra_auto),
    #-----------Analiticas--------------------------------
    path('analiticas/cantidad_compras/cantidad_compras_hoy/', cantidad_compras_hoy),
    path('analiticas/cantidad_compras/compras_dia_semana/', compras_dia_semana),
    path('analiticas/cantidad_compras/total_compras_mes/', total_compras_mes),
    path('analiticas/cantidad_compras/total_compras_mes_x_semana/', total_compras_mes_x_semana),
    path('analiticas/cantidad_compras/total_compras_mes_anterior_x_semana/', total_compras_mes_anterior_x_semana),
    path('analiticas/cantidad_compras/compras_por_mes_anual/', compras_por_mes_anual),
    path('analiticas/cantidad_compras/total_compras_semana_anual/', total_compras_semana_anual),
    path('analiticas/total_compras/total_compras_hoy/', total_compras_hoy),
    path('analiticas/total_compras/total_compra_semanal/', sum_total_compra_week),
    path('analiticas/total_compras/total_compra_diaria_semanal/', total_compra_diaria_semanal),
    path('analiticas/total_compras/total_compra_semanal_anual/', total_compra_semanal_anual),
    path('analiticas/total_compras/total_compra_semanal_mes/', total_compra_semanal_mes),
    path('analiticas/total_compras/total_compra_semanal_mes_anterior/', total_compra_semanal_mes_anterior),
    path('analiticas/total_compras/total_compras_por_mes_anual/', total_compras_por_mes_anual),
]