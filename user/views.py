from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from django.http import HttpResponseRedirect



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



# def logout(request):
#     return render(request, "user/logout.html")
