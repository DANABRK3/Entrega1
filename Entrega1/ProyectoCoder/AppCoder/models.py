from django.db import models
from datetime import datetime as dt
# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    comision=models.IntegerField()
    fecha_creacion=models.DateField(default=dt.now())
    dia_semana=models.IntegerField()

class Productos(models.Model):
    categoria=models.CharField(max_length=40)
    rango_precio=models.IntegerField()
    
class Vendedores(models.Model):
    localidad=models.CharField(max_length=40)
    tiempo_de_entrega=models.IntegerField()
    calificacion=models.IntegerField()
