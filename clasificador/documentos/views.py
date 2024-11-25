from django.shortcuts import render, redirect
from .forms import DocumentoForm
from .models import Documento
from .utils import clasificar_archivo

def cargar_archivo(request):
    if request.method == "POST":
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            documento = form.save()
            archivo_path = documento.archivo.path
            clasificacion, puntaje = clasificar_archivo(archivo_path)
            documento.clasificacion = clasificacion
            documento.puntaje = puntaje
            documento.save()
            return redirect('listar_documentos')
    else:
        form = DocumentoForm()
    return render(request, 'cargar_archivo.html', {'form': form})

def listar_documentos(request):
    documentos = Documento.objects.all()
    return render(request, 'listar_documentos.html', {'documentos': documentos})
