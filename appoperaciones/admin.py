from django.contrib import admin

# Register your models here.
from .models import Asistentes,Microfonistas,Camarografos

class AsistentesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido")
    list_filter = ("nombre", "apellido")
    
class MicrofonistasAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido")
    list_filter = ("nombre", "apellido")

class CamarografosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido")
    list_filter = ("nombre", "apellido")



# Register your models here.
admin.site.register(Asistentes,AsistentesAdmin)
admin.site.register(Microfonistas,MicrofonistasAdmin)
admin.site.register(Camarografos,CamarografosAdmin)
