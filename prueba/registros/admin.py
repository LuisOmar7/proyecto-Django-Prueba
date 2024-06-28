from django.contrib import admin
from .models import Alumnos
from .models import Comentario
from .models import ComentarioContacto

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    list_display = ('matrucula', 'nombre', 'carrera', 'turno')
    search_fields = ('matrucula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')

admin.site.register(Alumnos,AdministrarModelo)


class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields= ('created', 'id')

admin.site.register(Comentario, AdministrarComentarios)


class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'mensaje')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields= ('created', 'id')

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)