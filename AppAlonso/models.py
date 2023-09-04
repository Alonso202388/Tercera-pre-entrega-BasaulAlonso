from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()
    
class Estudiante(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
    
class Profesor(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    profesion = models.CharField(max_length=30)
    
        
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Entregable(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.fechaDeEntrega} {self.entregado}'
   
    

