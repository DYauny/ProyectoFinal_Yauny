from django.shortcuts import render
from .models import Asistentes, Camarografos, Microfonistas
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



# Asistentes

class AsistentesListView(LoginRequiredMixin, ListView):
    model = Asistentes
    context_object_name ="asistentes"
    template_name = "appoperaciones/Vistas_Clases/asistentes_lista.html"


class AsistentesDetalle(DetailView):
    model = Asistentes
    template_name = "appoperaciones/Vistas_Clases/asistentes_detalle.html"


class AsistentesCreateView(CreateView):
    model = Asistentes
    template_name = "appoperaciones/Vistas_Clases/asistentes_crear.html"
    success_url = reverse_lazy("Lista")
    fields = ["nombre", "apellido", "legajo"]


class AsistentesUpdateView(UpdateView):
    model = Asistentes
    template_name = "appoperaciones/Vistas_Clases/asistentes_actualizar.html"
    success_url = reverse_lazy("Lista")
    fields = ["nombre", "apellido", "legajo"]


class AsistentesDeleteView(DeleteView):
    model = Asistentes
    success_url = reverse_lazy("Lista")
    template_name = "appoperaciones/Vistas_Clases/asistentes_eliminar.html"
    
    
    
# Camarografos
   
class CamarografosListView(LoginRequiredMixin, ListView):
    model = Camarografos
    context_object_name ="camarografos"
    template_name = "appoperaciones/Vistas_Clases/camarografos_lista.html"


class CamarografosDetalle(DetailView):
    model = Camarografos
    template_name = "appoperaciones/Vistas_Clases/camarografos_detalle.html"


class CamarografosCreateView(CreateView):
    model = Camarografos
    template_name = "appoperaciones/Vistas_Clases/camarografos_crear.html"
    success_url = reverse_lazy("CamarografoLista")
    fields = ["nombre", "apellido", "legajo"]


class CamarografosUpdateView(UpdateView):
    model = Camarografos
    template_name = "appoperaciones/Vistas_Clases/camarografos_actualizar.html"
    success_url = reverse_lazy("CamarografoLista")
    fields = ["nombre", "apellido", "legajo"]


class CamarografosDeleteView(DeleteView):
    model = Camarografos
    success_url = reverse_lazy("CamarografoLista")
    template_name = "appoperaciones/Vistas_Clases/camarografos_eliminar.html"
    
    
    
# Microfonistas  
 
class MicrofonistasListView(LoginRequiredMixin, ListView):
    model = Microfonistas
    context_object_name ="microfonistas"
    template_name = "appoperaciones/Vistas_Clases/microfonistas_lista.html"


class MicrofonistasDetalle(DetailView):
    model = Microfonistas
    template_name = "appoperaciones/Vistas_Clases/microfonistas_detalle.html"


class MicrofonistasCreateView(CreateView):
    model = Microfonistas
    template_name = "appoperaciones/Vistas_Clases/microfonistas_crear.html"
    success_url = reverse_lazy("MicrofonistaLista")
    fields = ["nombre", "apellido", "legajo"]


class MicrofonistasUpdateView(UpdateView):
    model = Microfonistas
    template_name = "appoperaciones/Vistas_Clases/microfonistas_actualizar.html"
    success_url = reverse_lazy("MicrofonistaLista")
    fields = ["nombre", "apellido", "legajo"]


class MicrofonistasDeleteView(DeleteView):
    model = Microfonistas
    success_url = reverse_lazy("MicrofonistaLista")
    template_name = "appoperaciones/Vistas_Clases/microfonistas_eliminar.html"
    
    
    