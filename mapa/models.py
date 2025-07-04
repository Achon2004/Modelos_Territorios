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

class Manzana(models.Model):
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    numero = models.CharField(max_length=100)

    def __str__(self):
        return self.numero

class RegistroManzana(models.Model):
    manzana = models.ForeignKey(Manzana, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Capitan, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Registro {self.id} - {self.manzana} por {self.usuario}"
    
class HistorialCambio(models.Model):
    registro = models.ForeignKey(RegistroManzana, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Capitan, on_delete=models.CASCADE)
    accion = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.accion} - {self.fecha}"