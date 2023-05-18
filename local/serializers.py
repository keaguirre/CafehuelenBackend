from rest_framework import serializers
from .models import Local, Totem, Superv_local

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ('id_local', 'nombre_local', 'fono_local', 'direccion_local', 'estado')
        
class TotemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Totem
        fields = ( 'num_totem', 'mac_totem', 'local_asignado', 'estado')

class Superv_localSerializer(serializers.ModelSerializer):
    class Meta:
        model = Superv_local
        fields = ('usuario', 'contrasena', 'local_asignado', 'estado')

