from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Curso, Profesor, Estudiante, Entregable
from.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, EntregableFormulario
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def curso(req, nombre, camada): 
    
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    
    return HttpResponse(f"""
        <p>Curso: {curso.nombre} - Camada: {curso.camada} agregado!</p>                            
    """)
    
def lista_cursos(req):
    
    lista = Curso.objects.all()
    
    return render(req, "lista_cursos.html", {"lista_cursos": lista})


def inicio(req):
    
    return render(req, "inicio.html")

def cursos(req):
    
    return render(req, "cursos.html")

def profesores(req, nombre, apellido, email, profesion):
    
    profesor = Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion )
    profesor.save()
    
    return render(req, "profesores.html")

def estudiantes(req, nombre, apellido, email):
    
    estudiante = Estudiante(nombre=nombre, apellido=apellido, email=email)
    estudiante.save()
    
    return render(req, "estudiantes.html")

def entregables(req):
    
    return render(req, "entregables.html")

def curso_formulario(req: HttpRequest):
    
    print("method", req.method)
    print("post", req.POST)
    
    if req.method == "POST":
        
        miformulario = CursoFormulario(req.POST)
        
        if miformulario.is_valid():
            
            print(miformulario.cleaned_data)
            data = miformulario.cleaned_data
            
            curso = Curso(nombre=data["curso"], camada=data["camada"])
            curso.save()
            return render(req, "inicio.html", {"mensaje": "Curso creado con exito"})
        else:
            return render(req, "inicio.html", {"mensaje": "formulario inavalido"})
    else:
        
        miformulario = CursoFormulario()
        
        return render(req, "curso_formulario.html", {"miformulario": miformulario})
    
    
    
def profesor_formulario(request):
    if request.method == "POST":
        form = ProfesorFormulario(request.POST)
        if form.is_valid():
            # Crear una instancia de Profesor con los datos del formulario
            profesor = Profesor(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                profesion=form.cleaned_data['profesion']
            )
            profesor.save()
            return render(request, "inicio.html", {"mensaje": "Profesor creado con éxito"})
    else:
        form = ProfesorFormulario()
    
    return render(request, "profesor_formulario.html", {"form": form})

def estudiante_formulario(request):
    if request.method == "POST":
        form = EstudianteFormulario(request.POST)
        if form.is_valid():
            # Crear una instancia de Profesor con los datos del formulario
            estudiante = Estudiante(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email']   
            )
            estudiante.save()
            return render(request, "inicio.html", {"mensaje": "Estudiante creado con éxito"})
    else:
        form = EstudianteFormulario()
    
    return render(request, "estudiante_formulario.html", {"form": form})

def entregable_formulario(request):
    if request.method == "POST":
        form = EntregableFormulario(request.POST)
        if form.is_valid():
            # Crear una instancia de Profesor con los datos del formulario
            entregable = Entregable(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                fechaDeEntrega = form.cleaned_data['fechaDeEntrega'],
                entregado=form.cleaned_data['entregado']   
            )
            entregable.save()
            return render(request, "entregable_formulario.html", {"mensaje": "Entregable creado con éxito"})
    else:
        form = EntregableFormulario()
    
    return render(request, "entregable_formulario.html", {"form": form})


def busqueda_camada(req):
    
    return render(req, "busquedacamada.html")


def buscar(req):
    camada = req.GET.get("camada")
    
    if camada:
        try:
            curso = Curso.objects.get(camada=camada)
            return render(req, "resultadobusqueda.html", {"curso": curso})
        except ObjectDoesNotExist:
            return HttpResponse("No se encontró ningún curso con la camada especificada.")
    else:
        return HttpResponse("No ingresaste una camada en la búsqueda.")


    
    

