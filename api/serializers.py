from rest_framework import serializers
from .models import Cliente, Cotizacion

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class CotizacionSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)

    class Meta:
        model = Cotizacion
        fields = ['id', 'descripcion', 'estado', 'monto', 'fecha', 'cliente', 'cliente_nombre']

