from django.urls import path

from appoperaciones.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("asistentes/", asistentes, name="asistentes"),
    path("microfonistas/", microfonistas, name="microfonistas"),
    path("camarografos/", camarografos, name="camarografos"),
    #path("asistentesformulario/", asistentesFormulario, name="asistentesformulario"),
]