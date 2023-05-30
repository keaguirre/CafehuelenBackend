from django.urls import path, include
# bloque productos = Local, Totem, Supervisores_local
from .views import local_list, local_detail, superv_local_list, superv_local_detail, superv_local_login
urlpatterns = [
    path('locales/', local_list),
    path('locales/<int:id_local>', local_detail),
    path('supervisores_local/', superv_local_list),
    path('supervisores_local/<str:usuario>', superv_local_detail),
    path('supervisores_login/<str:usuario>', superv_local_login),
    # path('totems/', totem_list),
    # path('totems/<str:mac_totem>',totem_detail),
]