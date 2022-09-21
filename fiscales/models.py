from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Fiscales(models.Model):
    nombre_sucursal = models.CharField(max_length=50) #le pasamos el tipo de dato de cada variable
    numero_sucursal = models.CharField(max_length=5)
    modelo_fiscal = models.CharField(max_length=40)
    vencimiento_certificado_digital = models.DateField(blank=True,null=True)
    punto_venta = models.IntegerField()
    numero_serie = models.IntegerField()
    fecha_cambio = models.DateField()
    estado = models.CharField(max_length=40)


class Backups(models.Model):
    nombre_sucursal = models.CharField(max_length=50)
    numero_sucursal = models.CharField(max_length=5)
    nombre_archivo = models.CharField(max_length=40)
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()
    size_archivo = models.CharField(max_length=40)
    link = models.CharField(max_length=40)
