from django.db import models
from django.contrib.auth.models import User

class Contactos(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    motivo = models.CharField(max_length=500)
    estado = models.CharField(max_length=200,default='')