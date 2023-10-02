from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Curso, Profesor, Estudiante, Entregable
from.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, EntregableFormulario
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView


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

def profesores(req):
      
    return render(req, "profesores.html")

def estudiantes(req):
    
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

def listaProfesores(req):
    
    profesores = Profesor.objects.all()
    
    return render(req, "leerProfesores.html", {"profesores": profesores})

def crea_profesor(req):
    
    if req.method == "POST" :
        
        miFormulario = ProfesorFormulario(req.POST)
        
        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
                       
            profesor = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"])
            profesor.save()
            return render(req, "inicio.html", {"mensaje": "Profesor creado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:
        
        miFormulario = ProfesorFormulario()
        
        return render(req, "profesor_formulario.html", {"profesores": miFormulario})
            
def eliminaProfesor(req, id):
    
    if req.method == "POST":
        
        profesor = Profesor.objects.get(id=id)
        profesor.delete()
        
        profesores = Profesor.objects.all()
        
        return render(req, "leerProfesores.html", {"profesores": profesores})
            
def editarProfesor (req, id):
    
    profesor = Profesor.objects.get(id=id)
    
    if req.method == "POST":
        
        miFormulario = ProfesorFormulario(req.POST)
        
        if miFormulario.is_valid():
            
            data= miFormulario.changed_data
            
            profesor.nombre = data["nombre"]
            profesor.apellido = data["apellido"]
            profesor.email = data["email"]
            profesor.profesion = data["profesion"]
            profesor.save()
            return render(req, "inicio.html", {"mensaje": "Profesor actualizado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:
        
        miFormulario = ProfesorFormulario(initial={
            "nombre": profesor.nombre,
            "apellido": profesor.apellido,
            "email": profesor.email,
            "profesion": profesor.profesion,            
        })
            
        return render(req, "editarProfesor.html", {"miFormulario": miFormulario, "id": profesor.id})

class CursoList(ListView):
    model = Curso
    template_name = "curso_list.html"
    context_object_name = "cursos"
    
class CursoDetail(DetailView):
    model = Curso
    template_name = "curso_datail.html"
    context_object_name = "curso"
    
class CursoCreate(CreateView):
    model = Curso
    template_name = "curso_create.html"
    fields = ["nombre", "camada"]
    success_url = "/app-alonso/lista-curso/"

class CursoUpdate(UpdateView):
    model = Curso
    template_name = "curso_update.html"
    fields = ("__all__")
    success_url = "/app-alonso/lista-curso/"

class CursoDelete(DeleteView):
    model = Curso
    template_name = "curso_delete.html"
    success_url = "/app-alonso/"