from django.db import models

# Create your models here.
class Estacionamiento(models.Model):
    piso=models.CharField(primary_key=True,max_length=1)
    estado=models.BooleanField(default=False)
    tipos1=[
        ('Vip','Vip'),
        ('C','Colaborador'),
        ('V','Visita')
    ]
    tipo1=models.CharField(max_length=3,choices=tipos1)
    tipos2=[
        ('A','Auto'),
        ('B','Bus'),
        ('M','Moto'),
        ('C','Bicicleta')
    ]
    tipo2=models.CharField(max_length=3,choices=tipos2)
    telefono=models.CharField(max_length=9)
    