from django.urls import path, include
from .views import home, bienvenido, logouta, MiVistaProtegida

urlpatterns = [
    path("home/", home, name="home"),
    path("bienvenido/", bienvenido, name="bienvenido"),
    path("accounts/", include('django.contrib.auth.urls')),
    path("logout-a/", logouta, name="logout-a"),
    path("vista-protegida/", MiVistaProtegida.as_view(), name="vista_protegida"),
]