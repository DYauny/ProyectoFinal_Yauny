from django import forms
#from .models import Asistentes

class AsistenteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    legajo = forms.IntegerField()
      
      
class BuscaAsistenteForm(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()  
    