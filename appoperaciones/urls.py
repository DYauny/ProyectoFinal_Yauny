from django.urls import path

from appoperaciones.views import *
from appoperaciones import views_clases

urlpatterns = [
    path("", inicio, name="inicio"),
    path("nosotros/", nosotros, name="nosotros"),
    path("asistentes/", asistentes, name="asistentes"),
    path("microfonistas/", microfonistas, name="microfonistas"),
    path("camarografos/", camarografos, name="camarografos"),
    path('form-con-api/', form_con_api, name="form-con-api"),
    path('buscar/', buscar, name="buscar"),
    
    
    #path("asistentesformulario/", asistentesFormulario, name="asistentesformulario"),
]




urls_vistas_clases = [
    path("asistentes-lista/", views_clases.AsistentesListView.as_view(), name="Lista"),
    #path("clases/detalle/<pk>/", views_clases.CursoDetalle.as_view(), name="BorrarAsistente"),
    path("crear/", views_clases.AsistentesCreateView.as_view(), name="CrearAsistente"),
    path("actualizar/<pk>", views_clases.AsistentesUpdateView.as_view(), name="ActualizarAsistente"),
    path("eliminar/<pk>", views_clases.AsistentesDeleteView.as_view(), name="EliminarAsistente"),
]

urlpatterns += urls_vistas_clases