from django.shortcuts import render
from .models import Alumnos
from .forms import CometarioContactoForm
from .models import ComentarioContacto

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
            return render(request, 'registros/contacto.html')
    form = CometarioContactoForm()
    return render(request, 'registros/contacto.html', {'form': form})

def contacto(request):
    return render(request, 'registros/contacto.html')