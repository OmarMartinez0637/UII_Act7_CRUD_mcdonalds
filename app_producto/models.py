from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return f'Producto: {self.nombre} - {self.categoria}'
