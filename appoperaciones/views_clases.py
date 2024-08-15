from django.shortcuts import render
from .models import Asistentes
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin





class AsistentesListView(LoginRequiredMixin, ListView):
    model = Asistentes
    context_object_name ="asistentes"
    template_name = "appoperaciones/Vistas_Clases/asistentes_lista.html"


# class CursoDetalle(DetailView):
#     model = Curso
#     template_name = "AppCoder/Vistas_Clases/curso_detalle.html"


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
    
    
    
    