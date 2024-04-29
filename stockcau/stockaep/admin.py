from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Tecnico)
admin.site.register(Tipo)
admin.site.register(Hardware)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Notificacion)
admin.site.register(Asignacion)
admin.site.register(Ubicacion)