from rest_framework import serializers
from .models import Agricultor

class AgricultorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agricultor
        fields = '__all__'

class CultivoSerializer(serializers.ModelSerializer):
    agricultor_nombre = serializers.ReadOnlyField(source='agricultor.nombre')

    class Meta:
        model = Cultivo
        fields = ['id', 'nombre', 'tipo', 'cantidad', 'disponible', 'agricultor', 'agricultor_nombre']