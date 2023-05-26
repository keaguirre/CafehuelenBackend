from django.urls import path, include
# bloque productos = Local, Totem, Supervisores_local
from .views import local_list, local_detail, superv_local_list, superv_local_detail
urlpatterns = [
    path('local/', local_list),
    path('local/<int:id_local>', local_detail),
    path('superv_local/', superv_local_list),
    path('superv_local/<str:usuario>', superv_local_detail),
    # path('totem/', totem_list),
    # path('totem/<str:mac_totem>',totem_detail),
]