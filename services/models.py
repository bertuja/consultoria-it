from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Service(models.Model):
    CATEGORIAS = [
        ('devops', 'DevOps'),
        ('infra', 'Infraestructura'),
        ('seguridad', 'Seguridad'),
        ('desarrollo', 'Desarrollo'),
        ('cloud', 'Cloud'),
        ('datos', 'Datos'),
    ]

    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='servicios/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
