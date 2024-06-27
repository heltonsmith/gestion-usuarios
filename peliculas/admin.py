from django.contrib import admin
from .models import Pelicula

# Register your models here.
@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'anio_estreno', 'director', 'especial')