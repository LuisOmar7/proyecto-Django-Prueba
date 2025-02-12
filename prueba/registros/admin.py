from typing import Any
from .models import Comentario
from .models import ComentarioContacto

# Register your models here.
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from django.http import HttpResponse
from django.contrib import admin
from .models import Alumnos, Carrera


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

    def carrera_nombre(self, obj):
        """
        Método para mostrar el nombre de la carrera en la lista.
        """
        return obj.carrera.nombre if obj.carrera else "Sin carrera"
    carrera_nombre.short_description = 'Carrera'

    def get_queryset(self, request):
        """
        Filtra los registros de Alumnos según la carrera asignada al usuario actual.
        Optimiza la consulta usando select_related.
        """
        qs = super().get_queryset(request).select_related('carrera')  # Optimización de consultas
        user = request.user

        if user.is_superuser:
            return qs

        # Verificar si el usuario tiene un perfil asignado
        try:
            profile = user.profile
        except Profile.DoesNotExist:
            return qs.none()  # Devolver un queryset vacío si no hay perfil

        # Filtrar por la carrera asignada en el perfil del usuario
        if profile.carrera:
            return qs.filter(carrera=profile.carrera)
        else:
            return qs.none()  # Devolver un queryset vacío si no hay carrera asignada


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

class AdministrarCarreras(admin.ModelAdmin):
    list_display = ('id', 'nombre')

admin.site.register(Carrera, AdministrarCarreras)


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

# Crear un Inline para el modelo Profilefrom django.contrib import admin
# Inline para el modelo Profile
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Perfil'

    # Filtrar las carreras disponibles en el campo "carrera"
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "carrera":
            kwargs["queryset"] = Carrera.objects.all()  # Mostrar todas las carreras registradas
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

# Extender el UserAdmin para incluir el perfil
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

# Desregistrar el UserAdmin predeterminado y registrar el personalizado
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
