from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Fiscales(models.Model):
    nombre_suc = models.CharField(max_length=50) #le pasamos el tipo de dato de cada variable
    nro_suc = models.IntegerField()
    modelo_fiscal = models.CharField(max_length=40)
    punto_venta = models.IntegerField()
    nro_serie = models.IntegerField()
    fecha_cambio = models.DateField()
    estado = models.CharField(max_length=40)
