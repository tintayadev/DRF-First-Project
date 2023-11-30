from django.db import models

# Create your models here.
class Tarea(models.Model):
    nombre = models.CharField(max_length=10)
    completada = models.BooleanField(default=False)

    # class Meta:
    #     app_label = 'rest'

