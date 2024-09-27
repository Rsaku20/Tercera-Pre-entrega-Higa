from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('profesores/', profesores, name='Profesores'),
    path('cursos/', cursos, name="Cursos"),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('curso-formulario/', curso_formulario, name='CursoFormulario'), #Agregar cursos
    path('busqueda-curso/', busqueda_curso, name='BusquedaCurso'), #buscar que contenga y devuelve resultado
    path('buscar-curso/', buscar_curso, name='BuscarCurso'), #definir
    
]

