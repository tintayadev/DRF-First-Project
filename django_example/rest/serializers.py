from rest_framework import serializers
from .models import Tarea


class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__' #['id', 'completada', 'nombre', 'fecha_limite', 'descripcion'] # '__all__'
