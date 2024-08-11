from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "appoperaciones/inicio.html")

def asistentes(request):
    return render(request, "appoperaciones/asistentes.html")

def camarografos(request):
    return render(request, "appoperaciones/camarografos.html")

def microfonistas(request):
    return render(request, "appoperaciones/microfonistas.html")




# from appoperaciones.models import Asistentes

# def asistentesFormulario(request):
    
#     if request.method == 'POST':
        
#         asistentes = Asistentes (nombre=request.POST['nombre'],apellido=request.POST['apellido'])
#         asistentes.save()
        
#         return render (request, "appoperaciones/inicio.html")
    
#     return render(request, "appoperaciones/asistentesformulario.html")