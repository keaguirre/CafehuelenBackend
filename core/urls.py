from django.urls import path, include
from .views import home, homeApi

urlpatterns = [
    path('',home),    
    path('api/',homeApi),    
]