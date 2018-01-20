from django.db import models

from apps.adopcion.models import Persona
# Create your models here.

#Moelo es como una tabla
class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    # para el modelo uno a muchos 1 persona Varios mascotas:
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    # para el modelo muchos a muchos:
    vacuna = models.ManyToManyField(Vacuna, blank=True)

