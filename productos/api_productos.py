from .models import Categoria, Ingrediente, Detalle_preparacion, Preparacion
from rest_framework import viewsets, permissions
from .serializers import CategoriaSerializer, IngredienteSerializer, Detalle_preparacionSerializer, PreparacionSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoriaSerializer

class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = IngredienteSerializer

class Detalle_preparacionViewSet(viewsets.ModelViewSet):
    queryset = Detalle_preparacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Detalle_preparacionSerializer

class PreparacionViewSet(viewsets.ModelViewSet):
    queryset = Preparacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PreparacionSerializer