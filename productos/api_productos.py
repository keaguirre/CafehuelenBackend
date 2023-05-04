from .models import categoria, ingrediente, detalle_preparacion, preparacion
from rest_framework import viewsets, permissions
from .serializers import categoriaSerializer, ingredienteSerializer, detalle_preparacionSerializer, preparacionSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = categoria.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = categoriaSerializer

class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = ingrediente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ingredienteSerializer

class Detalle_preparacionViewSet(viewsets.ModelViewSet):
    queryset = detalle_preparacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = detalle_preparacionSerializer

class PreparacionViewSet(viewsets.ModelViewSet):
    queryset = preparacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = preparacionSerializer