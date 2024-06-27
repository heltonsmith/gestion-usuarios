from django.db import models

# Create your models here.
class Pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    anio_estreno = models.IntegerField()
    director = models.CharField(max_length=100)
    especial = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre