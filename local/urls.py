from django.urls import path, include
# bloque productos = Local, Totem, Supervisores_local, Proveedor
from .views import local_list, local_detail, totem_list, totem_detail, superv_local_list, superv_local_detail, proveedor_list, proveedor_detail
urlpatterns = [
    path('local/', local_list),
    path('local/<int:id_local>', local_detail),
    path('totem/', totem_list),
    path('totem/<int:num_totem>',totem_detail),
    path('superv_local/', superv_local_list),
    path('superv_local/<str:usuario>', superv_local_detail),
    path('proveedor/', proveedor_list),
    path('proveedor/<int:id_proveedor>', proveedor_detail),
]