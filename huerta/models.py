from django.db import models

class Agricultor(models.Model):
    nombre = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.barrio})"

class Cultivo(models.Model):
    TIPOS_OFERTA = [
        ('semilla', 'Semilla'),
        ('cosecha', 'Cosecha'),
        ('plantula', 'Plántula'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS_OFERTA, default='cosecha')
    cantidad = models.CharField(max_length=50)
    disponible = models.BooleanField(default=True)
    agricultor = models.ForeignKey(
        Agricultor,
        on_delete=models.CASCADE,
        related_name='cultivos'
    )

    def _str_(self):
        return f"{self.nombre} - {self.agricultor.nombre}"