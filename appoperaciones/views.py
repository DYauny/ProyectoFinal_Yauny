from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from appoperaciones.models import Asistentes
from appoperaciones.forms import AsistenteFormulario, BuscaAsistenteForm




# Create your views here.
def inicio(request):
    return render(request, "appoperaciones/inicio.html")


@login_required
def nosotros(request):
    return render(request, "appoperaciones/nosotros.html")


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

            asistente = Asistentes(nombre=informacion["nombre"], apellido=informacion["apellido"], legajo=informacion["legajo"])
            asistente.save()

            return render(request, "appoperaciones/inicio.html")
    else:
        mi_formulario = AsistenteFormulario()

    return render(request, "appoperaciones/form_con_api.html", {"mi_formulario": mi_formulario})



# def busquedaapellido(request):
#     return render(request, "appoperaciones/busquedaapellido.html")

# def buscar(request):
#       respuesta = F"Estoy buscando el apellido: {request.GET['apellido']}"
      
#       return HttpResponse(respuesta)


def buscar(request):
    if request.method == "POST":
        miFormulario = BuscaAsistenteForm(request.POST) # Aqui me llega la informacion del html

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            print(miFormulario)
            
            
            asistentes = Asistentes.objects.filter(apellido__icontains=informacion["apellido"])
                                                  #apellido__icontains=informacion["apellido"])

        return render(request, "appoperaciones/resultado.html", {"asistentes": asistentes})
    else:
         miFormulario = BuscaAsistenteForm()
         
    return render(request, "appoperaciones/busqueda.html", {"miFormulario": miFormulario})
  
  
 



