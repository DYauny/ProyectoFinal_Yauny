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



# Asistentes
urls_Asistentes = [
    path("asistentes-lista/", views_clases.AsistentesListView.as_view(), name="Lista"),
    path("detalles/<pk>/", views_clases.AsistentesDetalle.as_view(), name="Detalles"),
    path("crear/", views_clases.AsistentesCreateView.as_view(), name="CrearAsistente"),
    path("actualizar/<pk>", views_clases.AsistentesUpdateView.as_view(), name="ActualizarAsistente"),
    path("eliminar/<pk>", views_clases.AsistentesDeleteView.as_view(), name="EliminarAsistente"),
]
urlpatterns += urls_Asistentes


# Camarografos
urls_Camarografos = [
    path("camarografos-lista/", views_clases.CamarografosListView.as_view(), name="CamarografoLista"),
    path("camarografo-detalles/<pk>/", views_clases.CamarografosDetalle.as_view(), name="CamarografoDetalles"),
    path("camarografo-crear/", views_clases.CamarografosCreateView.as_view(), name="CamarografoCrear"),
    path("camarografo-actualizar/<pk>", views_clases.CamarografosUpdateView.as_view(), name="CamarografoActualizar"),
    path("camarografo-eliminar/<pk>", views_clases.CamarografosDeleteView.as_view(), name="CamarografoEliminar"),
]
urlpatterns += urls_Camarografos


#Microfonistas
urls_Microfonistas = [
    path("microfonistas-lista/", views_clases.MicrofonistasListView.as_view(), name="MicrofonistaLista"),
    path("microfonista-detalles/<pk>/", views_clases.MicrofonistasDetalle.as_view(), name="MicrofonistaDetalles"),
    path("microfonista-crear/", views_clases.MicrofonistasCreateView.as_view(), name="MicrofonistaCrear"),
    path("microfonista-actualizar/<pk>", views_clases.MicrofonistasUpdateView.as_view(), name="MicrofonistaActualizar"),
    path("microfonista-eliminar/<pk>", views_clases.MicrofonistasDeleteView.as_view(), name="MicrofonistaEliminar"),
]
urlpatterns += urls_Microfonistas