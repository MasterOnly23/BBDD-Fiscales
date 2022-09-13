from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField(max_length=40) #le pasamos el tipo de dato de cada variable
    apellido = models.CharField(max_length=40)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField()
