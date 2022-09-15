from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Fiscales(models.Model):
    nombre_sucursal = models.CharField(max_length=50) #le pasamos el tipo de dato de cada variable
    numero_sucursal = models.IntegerField()
    modelo_fiscal = models.CharField(max_length=40)
    punto_venta = models.IntegerField()
    numero_serie = models.IntegerField()
    fecha_cambio = models.DateField()
    estado = models.CharField(max_length=40)
