from django.db import models

# Create your models here.
class Receta(models.Model):
    nombre = models.CharField(max_length=150)
    chef = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()
    imagen = models.ImageField(upload_to='recetas/')
    categoria = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self): #Mostrar recetas tal cual (como texto)
        return self.nombre