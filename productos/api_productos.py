from .models import Categoria, Ingrediente, Ingredientes_preparacion, Preparacion
from rest_framework import viewsets, permissions
from .serializers import CategoriaSerializer, IngredienteSerializer, Ingredientes_preparacionSerializer, PreparacionSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoriaSerializer

class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = IngredienteSerializer

class Ingredientes_preparacionViewSet(viewsets.ModelViewSet):
    queryset = Ingredientes_preparacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Ingredientes_preparacionSerializer

class PreparacionViewSet(viewsets.ModelViewSet):
    queryset = Preparacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PreparacionSerializer