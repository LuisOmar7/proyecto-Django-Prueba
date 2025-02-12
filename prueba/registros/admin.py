from typing import Any
from .models import Comentario
from .models import ComentarioContacto

# Register your models here.
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from django.http import HttpResponse
from django.contrib import admin
from .models import Alumnos


from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile


# Función para generar PDF 
def generar_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="alumno.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    for alumno in queryset:
        p.drawString(100, height - 70, "Datos del Alumno")
        y = height - 50
        imagen = ImageReader(alumno.imagen.path)
        p.drawImage(imagen, 100, height - 200, width=100, height=100)
        y = height - 220
        p.drawString(100, y, f"Matrícula: {alumno.matrucula}")
        p.drawString(100, y - 20, f"Nombre: {alumno.nombre}")
        p.drawString(100, y - 40, f"Carrera: {alumno.carrera}")
        p.drawString(100, y - 60, f"Turno: {alumno.turno}")
      
        p.showPage()

    p.save()
    return response

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'update')  # Campos de solo lectura
    list_display = ('matrucula', 'nombre', 'carrera', 'turno')
    search_fields = ('matrucula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno', 'created')
    list_per_page = 5
    list_display_links = ('matrucula', 'nombre')
    list_editable = ('turno',)
    actions = [generar_pdf]


    def get_readonly_fields(self, request, obj=None):
        # Si se está editando un alumno existente, bloquear ciertos campos
        if obj is not None:
            if request.user.groups.filter(name="editores").exists():
                return ('matrucula','carrera', 'turno',) #Lo que si se muestra pero no es editable
            else:
                return ('created', 'update', 'imagen') #No se muestran los campos 
        # Si se está creando un nuevo alumno, no bloquear ningún campo
        else:
            return ()

admin.site.register(Alumnos, AdministrarModelo)


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

# Crear un Inline para el modelo Profile
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Perfil'

# Extender el UserAdmin para incluir el perfil
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

# Desregistrar el UserAdmin predeterminado y registrar el personalizado
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)