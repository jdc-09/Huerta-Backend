from django.db import models

class Agricultor(models.Model):
    nombre = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.barrio})"