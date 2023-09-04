from django.urls import path
from AppAlonso.views import curso, lista_cursos, inicio, cursos, estudiantes, profesores, entregables, curso_formulario, entregable_formulario, estudiante_formulario, profesor_formulario, busqueda_camada, buscar

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso, name="Curso"),
    path('lista-cursos/', lista_cursos, name="Lista-Cursos"),
    path('', inicio, name="Inicio"),
    path('cursos/', cursos, name="Cursos"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('profesores/', profesores, name="Profesores"),
    path('entregables/', entregables, name="Entregables"),
    path('curso-formulario/', curso_formulario, name="CursoFormulario"),
    path('busqueda-camada/', busqueda_camada, name="BusquedaCamada"),
    path('buscar/', buscar, name="Buscar"),
    path('profesor-formulario/', profesor_formulario, name="ProfesorFormulario"),
    path('estudiante-formulario/', estudiante_formulario, name="EstudianteFormulario"),
    path('entregable-formulario/', entregable_formulario, name="EntregableFormulario"),
    
]
