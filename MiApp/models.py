from django.db import models
from django.contrib.auth.admin import User


class escuela(models.Model):
    taller = models.CharField(max_length = 100)
    
class profesor(models.Model):
    nombre = models.CharField(max_length = 100)
    taller = models.CharField(max_length = 100)
    DNI = models.IntegerField()

    def __str__(self):
      return f"{self.nombre}, {self.taller}, {self.DNI}"


class alumno(models.Model):
    taller = models.CharField(max_length = 100)
    nombre = models.CharField(max_length = 100)
    DNI = models.IntegerField()
    
    
    

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
    texto = models.TextField(max_length=3000)
    publicado_el = models.DateField()
    imagen = models.ImageField(upload_to="posts", null=True, blank=True)

class WebSiteSetup(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)

class Mensaje(models.Model):
    email = models.EmailField()
    nombre = models.CharField(max_length=100)
    texto = models.TextField(max_length=3000)
    enviado_el = models.DateField(auto_now_add=True)

class Avatar(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='avatar')
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)