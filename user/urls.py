from django.urls import path
from django.contrib.auth.views import LogoutView
from user import views


urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', LogoutView.as_view(template_name="appoperaciones/inicio.html"), name= "Logout"),
    path('editarperfil/', views.editar_perfil, name="editarperfil"),
    path('cambiarcontrasenia/', views.CambiarContrasenia.as_view(), name="cambiarcontrasenia")
        
    
]
    
    