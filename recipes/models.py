from django.db import models

# Create your models here.
# Modelo de Receta
class Receta(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    instrucciones = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

# Modelo de Ingrediente
class Ingrediente(models.Model):
    receta = models.ForeignKey(Receta, related_name='ingredientes', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    cantidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.cantidad}"