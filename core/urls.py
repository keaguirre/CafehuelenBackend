from django.urls import path, include
from .views import home, homeApi, homeAnaliticas

urlpatterns = [
    path('',home),    
    path('api/',homeApi),    
    path('api/v1/analiticas',homeAnaliticas),    
]