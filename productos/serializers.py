from rest_framework import serializers
from .models import Categoria, Ingrediente, Detalle_preparacion, Preparacion

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id_cat', 'nombre_cat', 'estado')
        #read_only_fields = ('id_cat')

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('id_ingre', 'marca_ingre', 'nombre_ingre', 'stock_ingrediente', 'cantidad_por_unidad_ingrediente', 'tipo_unidad_ingrediente', 'imagen_ingre', 'fecha_creacion_ingre', 'fecha_actualizacion_ingre', 'estado')
        #read_only_fields = ('id_ingre')

class Detalle_preparacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_preparacion
        fields = ('id_detalle_prep', 'id_prep', 'id_ingre', 'cantidad_necesaria', 'tipo_unidad', 'estado')
        #read_only_fields = ('id_prep', 'id_ingre')

class PreparacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preparacion
        fields = ('id_prep', 'nombre_prep', 'descripcion_prep', 'imagen_prep', 'id_cat_prep', 'precio_prep', 'estado')
        #read_only_fields = ('id_prep')