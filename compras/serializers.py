from rest_framework import serializers
from .models import Compra, Item_compra



class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ('id_compra', 'tipo_servicio_compra', 'fecha_compra', 'estado_compra','total_compra', 'procesador_pago_compra', 'id_transaccion_compra', 'cod_comercio_compra', 'respuesta_tb_compra', 'respuesta_mp_compra', 'totem_compra')
        #read_only_fields = ('id_ingre')
class Item_compraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_compra
        fields = ('id_item_compra','id_prep', 'id_compra', 'cantidad_item', 'precio_unitario_item', 'total_item')
        #read_only_fields = ('id_prep', 'id_ingre')