from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
# models.py
from django.contrib.auth.models import User

class Carrera(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Carrera")

    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'

    def __str__(self):
        return self.nombre


class Alumnos(models.Model):
    matrucula = models.CharField(max_length=12, verbose_name='Matrícula')
    nombre = models.TextField(verbose_name='Nombre')
    carrera = models.ForeignKey(
        Carrera,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Carrera"
    )
    turno = models.CharField(max_length=10, verbose_name='Turno')
    imagen = models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografía')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update = models.DateTimeField(auto_now=True, verbose_name='Última actualización')

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['-created']

    def __str__(self):
        return self.nombre


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    carrera = models.ForeignKey(
        Carrera,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Carrera asignada"
    )

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return f"{self.user.username} - {self.carrera}"
    
class Comentario(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Clave')
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE, verbose_name='Alumno')
    created = models.DateField(auto_now_add=True, verbose_name='Registrado')
    coment = RichTextField(verbose_name='Comentario')

    class Meta: 
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-created']

    def __str__(self):
        return self.coment
    
class ComentarioContacto(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Clave')
    usuario = models.TextField(verbose_name='Usuario')
    mensaje = models.TextField(verbose_name='Comentario')
    created = models.DateField(auto_now_add=True, verbose_name='Registrado')

    class Meta:
        verbose_name = 'Comentario Contacto'
        verbose_name_plural = 'Comentarios Contactos'
        ordering = ['-created']

    def __str__(self):
        return self.mensaje
    
class Archivos(models.Model):
    id= models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    archivo = models.FileField(upload_to='archivos', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Archivo'
        verbose_name_plural = 'Archivos'
        ordering = ['-created']

    def __str__(self):
        return self.titulo
