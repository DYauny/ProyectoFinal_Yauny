from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from user.forms import UserEditForm, UserRegisterForm
#from user.models import Imagen


# Create your views here.
def login_request(request):

    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                next_url = request.GET.get("next", "/")
                return HttpResponseRedirect(next_url)

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "user/login.html", {"form": form, "msg_login": msg_login})


def register(request):
    
    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            
            form.save()
            return render(request,"appoperaciones/inicio.html")
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"user/registro.html" ,  {"form":form, "msg_register": msg_register})


@login_required
def editar_perfil (request):
    usuario = request.user
    
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)
        if miFormulario.is_valid():
            
            if miFormulario.cleaned_data.get('imagen'):
                usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                usuario.avatar.save()
            miFormulario.save()

            return render(request, "appoperaciones/inicio.html")

    else:
        miFormulario = UserEditForm(instance=usuario)

    return render(request, "user/editar_perfil.html", {"form": miFormulario})


class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "user/editar_pass.html"
    success_url = reverse_lazy("editarperfil")
