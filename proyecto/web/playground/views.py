from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def inicio(request):
    datos={'nombreapp':'playground','curso':'python'}
    return render(request,'inicio.html',datos)

def familia_formu(request):
    if request.method=='POST':
        form=formufamiliar(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion['nombre']
            apellido=informacion['apellido']
            edad=informacion['edad']
            email=informacion['email']
            nacimiento=informacion['nacimiento']
            familiar1=Familiar(nombre_familiar=nombre,apellido_familiar=apellido,email_familiar=email,edad_familiar=edad,nacimiento_familiar=nacimiento)
            familiar1.save()
            return render(request,'inicio.html',{'mensaje':'familiar creado'})
    else:
        formulario=formufamiliar()
    
    return render(request,'familiar.html',{'form':formulario})

def mascota_formu(request):
    if request.method=='POST':
        form=formumascota(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion['nombre']
            raza=informacion['raza']
            edad=informacion['edad']

            perrito=Mascota(nombre_mascota=nombre,edad_mascota=edad,raza_mascota=raza)
            perrito.save()
            return render(request,'inicio.html',{'mensaje':'has creado a tu mascota!!!'})
    else:
        formulario=formumascota()
    
    return render(request,'mascotas.html',{'form':formulario})

def estudios_formu(request):
    if request.method=='POST':
        form=formuestudios(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion['nombre']
            especialidad=informacion['especialidad']
            comision=informacion['comision']

            estudio1=Estudios(nombre_estudio=nombre,especialidad_estudio=especialidad,cantidad_estudios=comision)
            estudio1.save()
            return render(request,'inicio.html',{'mensaje':'has grabado correctamente tus estudios'})
    else:
        formulario=formuestudios()
    
    return render(request,'estudios.html',{'form':formulario})

def busqueda_mascota(request):
    return render(request,'busquedamascota.html')

def encontra_mascota(request):
    if request.GET['perritos']:
        perrito2=request.GET['perritos']
        perrito=Mascota.objects.filter(raza_mascota=perrito2)
        return render(request,'encontrarperrito.html',{'busqueda':perrito})
    else:
        return render(request,'busuquedamascota.html',{'mensaje':'ingrese una raza mascota para su busuqueda'})