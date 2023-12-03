from django.db import models

# Create your models here.
class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True) 
    fecha_limite = models.DateField(null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    completada = models.BooleanField(default=False)

    # class Meta:
    #     app_label = 'rest'

