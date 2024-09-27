from django.http import HttpResponse
from django.shortcuts import render

from app_coder.forms import CursoFormulario
from.models import Curso

# Create your views here.


def inicio(req):
    return render(req,"inicio.html",{})

def cursos(req):
    return render(req,"cursos.html",{})

def profesores(req):
    return render(req,"profesores.html",{})

def estudiantes(req):
    return render(req,"estudiantes.html",{})

def curso_formulario(req):

  print('method', req.method)
  print('data', req.POST)

  if req.method == 'POST':

    mi_formulario = CursoFormulario(req.POST)

    if mi_formulario.is_valid():

      data = mi_formulario.cleaned_data

      nuevo_curso = Curso(nombre=data["curso"], camada=data["camada"])
      nuevo_curso.save()

      return render(req, "inicio.html", {})
    
    else:
      return render(req, "curso_formulario.html", { "mi_formulario": mi_formulario })
  
  else:

    mi_formulario = CursoFormulario()
    return render(req, "curso_formulario.html", { "mi_formulario": mi_formulario })
  
def busqueda_curso(req):

  return render(req, "busqueda_curso.html")

def buscar_curso(req):

  nombre_curso = req.GET["nom_curso"]

  cursos = Curso.objects.filter(nombre__icontains=nombre_curso)

  return render(req, "resultado_busqueda.html", { "cursos": cursos, "nom_curso": nombre_curso })