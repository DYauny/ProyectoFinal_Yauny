from django.urls import path

from appoperaciones.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("asistentes/", asistentes, name="asistentes"),
    path("microfonistas/", microfonistas, name="microfonistas"),
    path("camarografos/", camarografos, name="camarografos"),
    path('form-con-api/', form_con_api, name="form-con-api"),
    path('busquedaapellido/', busquedaapellido, name="busquedaapellido"),
    path('buscar/', buscar, name="buscar"),
    
    
    #path("asistentesformulario/", asistentesFormulario, name="asistentesformulario"),
]