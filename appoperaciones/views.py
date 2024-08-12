from django.shortcuts import render
from appoperaciones.models import Asistentes
from appoperaciones.forms import AsistenteFormulario, BuscaAsistenteForm
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "appoperaciones/inicio.html")

def asistentes(request):
    return render(request, "appoperaciones/asistentes.html")

def camarografos(request):
    return render(request, "appoperaciones/camarografos.html")

def microfonistas(request):
    return render(request, "appoperaciones/microfonistas.html")




def form_con_api(request):
    if request.method == "POST":
        mi_formulario = AsistenteFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            asistente = Asistentes(nombre=informacion["nombre"], apellido=informacion["apellido"])
            asistente.save()

            return render(request, "appoperaciones/inicio.html")
    else:
        mi_formulario = AsistenteFormulario()

    return render(request, "appoperaciones/form_con_api.html", {"mi_formulario": mi_formulario})



def busquedaapellido(request):
    return render(request, "appoperaciones/busquedaapellido.html")

def buscar(request):
      respuesta = F"Estoy buscando el apellido: {request.GET['apellido']}"
      
      return HttpResponse(respuesta)


# def buscar(request):
#     if request.method == "POST":
#         miFormulario = BuscaAsistenteForm(request.POST) # Aqui me llega la informacion del html

#         if miFormulario.is_valid():
#             informacion = miFormulario.cleaned_data
            
#             asistentes = Asistentes.objects.filter(nombre__icontains=informacion["asistente"])

#             return render(request, "appoperaciones/mostrar_asistentes.html", {"asistentes": asistentes})
#     else:
#         miFormulario = BuscaAsistenteForm()

#     return render(request, "appoperaciones/buscar_form_con_api.html", {"miFormulario": miFormulario})



# from appoperaciones.models import Asistentes

# def asistentesFormulario(request):
    
#     if request.method == 'POST':
        
#         asistentes = Asistentes (nombre=request.POST['nombre'],apellido=request.POST['apellido'])
#         asistentes.save()
        
#         return render (request, "appoperaciones/inicio.html")
    
#     return render(request, "appoperaciones/asistentesformulario.html")