from django.db import models

# Create your models here.

class Capitan(models.Model): 
    nombre = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class Zona(models.Model):
    nombre = models.CharField(max_length=100)
    Descripción = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

