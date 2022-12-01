from django import forms

class formufamiliar(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    edad=forms.IntegerField()
    nacimiento=forms.DateField()

class formumascota(forms.Form):
    nombre=forms.CharField(max_length=50)
    raza=forms.CharField(max_length=50)
    edad=forms.IntegerField()

class formuestudios(forms.Form):
    nombre=forms.CharField(max_length=100)
    especialidad=forms.CharField(max_length=50)
    comision=forms.IntegerField()