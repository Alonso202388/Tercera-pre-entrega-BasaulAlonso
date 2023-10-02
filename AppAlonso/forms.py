from django import forms 

class CursoFormulario(forms.Form):
    
    curso = forms.CharField(required=True)
    camada = forms.IntegerField(required=True)

class ProfesorFormulario(forms.Form):
    
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)
    
class EstudianteFormulario(forms.Form):
    
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    
class EntregableFormulario(forms.Form):
    
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    fechaDeEntrega = forms.DateField(required=True) 
    entregado = forms.BooleanField(required=True)