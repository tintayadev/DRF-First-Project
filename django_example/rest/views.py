from django.shortcuts import render
from rest_framework import viewsets
from rest.models import Tarea
from rest.serializers import TareaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    @action(detail=False, methods=['GET'])
    def completadas(self, request):
        tareas_completadas = Tarea.objects.filter(completada=True)
        serializer = self.get_serializer(tareas_completadas, many=True)
        return Response(serializer.data)
