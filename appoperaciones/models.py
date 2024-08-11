from django.db import models

# Create your models here.

class Asistentes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    legajo= models.CharField(max_length=30)
    
    
    def __str__(self):
        return f"Nombre del Asistente: {self.nombre} - Apellido del Asistente: {self.apellido}"
    
class Camarografos(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    legajo= models.CharField(max_length=30)  
    

class Microfonistas(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    legajo= models.CharField(max_length=30)
    

