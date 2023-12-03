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
    lookup_field = 'id'

    @action(detail=False, methods=['GET'])
    def completadas(self, request):
        tareas_completadas = Tarea.objects.filter(completada=True)
        serializer = self.get_serializer(tareas_completadas, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['POST'])
    def crear_tarea(self, request):
        tarea_nueva = self.get_serializer(data=request.data)

        if tarea_nueva.is_valid():
            tarea_nueva.save()
            return Response(tarea_nueva.data, status=201)
        else:
            return Response(tarea_nueva.data, status=404)
        
    @action(detail=True, methods=['GET'])
    def detalle_tarea(self, request, id=None):
        tarea = self.get_object()
        serializer = self.get_serializer(tarea)
        return Response(serializer.data)

    @action(detail=True, methods=['PUT', 'PATCH'])
    def actualizar_tarea(self, request, id=None):
        tarea = self.get_object()
        serializer = self.get_serializer(tarea, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    @action(detail=True, methods=['DELETE'])
    def eliminar_tarea(self, request, id=None):
        tarea = self.get_object()
        tarea.delete()
        return Response("Eliminado correctamente", status=204)
    