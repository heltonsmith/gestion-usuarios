from django.shortcuts import render, redirect
from .models import Pelicula
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def bienvenido(request):
    todas_peliculas = Pelicula.objects.all()
    return render(request, 'bienvenido.html', {'peliculas': todas_peliculas})

def logouta(request):
    logout(request)
    return redirect('home')

class MiVistaProtegida(LoginRequiredMixin, TemplateView):
    template_name = 'mi_vista_protegida'