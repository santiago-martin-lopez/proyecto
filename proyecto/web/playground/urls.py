from django.urls import path
from .views import *
urlpatterns = [
    path('',inicio,name='inicio'),
    path('familiar/',familia_formu,name='familia'),
    path('/mascotas',mascota_formu,name='mascota'),
    path('estudios/',estudios_formu,name='estudios'),
    path('busquedamascota/',busqueda_mascota,name='busquedamascota'),
    path('encontrarperrito/',encontra_mascota,name='encontrarperrito')
]
