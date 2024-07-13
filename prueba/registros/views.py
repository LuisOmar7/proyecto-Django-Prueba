from django.shortcuts import render
from .models import Alumnos
from .forms import CometarioContactoForm
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404
import datetime
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages

# Create your views here.
def registros(request):
    alumnos=Alumnos.objects.all()
    return render(request, 'registros/principal.html', {'alumnos':alumnos})

def comentarios(request):
    comentarioss=ComentarioContacto.objects.all()
    return render(request, 'registros/comentarios.html', {'comentarios':comentarioss})

def registrar(request):
    if request.method == 'POST':
        form = CometarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            comentarioss=ComentarioContacto.objects.all()
            return render(request, 'registros/comentarios.html', {'comentarios':comentarioss})
    form = CometarioContactoForm()
    return render(request, 'registros/contacto.html', {'form': form})

def contacto(request):
    return render(request, 'registros/contacto.html')


def eliminarComentario(request, id, confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request, 'registros/comentarios.html', {'comentarios':comentarios})
    
    return render(request, confirmacion, {'object':comentario})

def consultarComentarioIndividual(request,id):
    comentario=ComentarioContacto.objects.get(id=id)

    return render(request, 'registros/formEditarComentario.html', {'comentario':comentario})

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = CometarioContactoForm(request.POST, instance=comentario)
    if form.is_valid():
        form.save()
        comentarios=ComentarioContacto.objects.all()
        return render(request, 'registros/comentarios.html', {'comentarios':comentarios})
    return render(request, 'registros/formEditarComentario.html', {'comentario':comentario})

def consultar1(request):
    alumnos=Alumnos.objects.filter(carrera='TI')
    return render(request, 'registros/consultas.html', {'alumnos':alumnos})

def consultar2(request):
    alumnos=Alumnos.objects.filter(carrera='TI').filter(turno='Matutino')
    return render(request, 'registros/consultas.html', {'alumnos':alumnos})

def consultar3(request):
    alumnos=Alumnos.objects.all().only('matrucula', 'nombre', 'carrera', 'turno', 'imagen')
    return render(request, 'registros/consultas.html', {'alumnos':alumnos})

def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains='Vesp')
    return render(request, 'registros/consultas.html', {'alumnos':alumnos})

def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=['Juan', 'Ana'])
    return render(request, 'registros/consultas.html', {'alumnos':alumnos})

def consultar6(request):
    fechainicio= datetime.date(2024, 7, 2)
    fechafin= datetime.date(2024, 7, 13)
    alumnos=Alumnos.objects.filter(created__range=[fechainicio, fechafin])
    return render(request, 'registros/consultas.html', {'alumnos':alumnos})

def consultar7(request):
    alumnos=Alumnos.objects.filter(comentario__coment__contains='No inscrito')
    return render(request, 'registros/consultas.html', {'alumnos':alumnos})

    
def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            return render(request,"registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        return render(request,"registros/archivos.html",{'archivo':Archivos})