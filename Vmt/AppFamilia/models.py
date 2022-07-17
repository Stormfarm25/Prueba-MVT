from django.db import models

# Create your models here.

class Padres(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    ocupacion = models.CharField(max_length=30)

class Hermanos(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    ocupacion = models.CharField(max_length=30)

class Abuelos(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    ocupacion = models.CharField(max_length=30)