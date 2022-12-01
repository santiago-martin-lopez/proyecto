from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre_familiar=models.CharField(max_length=50)
    apellido_familiar=models.CharField(max_length=50)
    email_familiar=models.EmailField()
    edad_familiar=models.IntegerField()
    nacimiento_familiar=models.DateField()

    def __str__(self):
        super().__str__()
        return f'nombre del familiar {self.nombre_familiar}'

class Mascota(models.Model):
    nombre_mascota=models.CharField(max_length=50)
    raza_mascota=models.CharField(max_length=50)
    edad_mascota=models.IntegerField()

    def __str__(self) -> str:
        super().__str__()
        return f'mi mascota se llama {self.nombre_mascota}'

class Estudios(models.Model):
    nombre_estudio=models.CharField(max_length=100)
    especialidad_estudio=models.CharField(max_length=50)
    cantidad_estudios=models.IntegerField()
