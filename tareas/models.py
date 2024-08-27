# models.py
from django.db import models
class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    estado = models.CharField(max_length=10, choices=[('pendiente', 'Pendiente'),
    ('completado', 'Completado')])

    def __str__(self):
        return self.titulo
