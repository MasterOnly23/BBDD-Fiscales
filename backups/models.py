from django.db import models

# Create your models here.


class Backups(models.Model):
    nombre_sucursal = models.CharField(max_length=50)
    link_backup = models.CharField(max_length=60)
    estado = models.CharField(max_length=40)
