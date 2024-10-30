from django.contrib import admin
from django.contrib import admin

# Register your models here.
from . import models 
class formacompanhamentoadmin(admin.ModelAdmin):
    list_display = ('data_inicio','data_final','prestador','agente','placa','id_equipamento','km_inicial','km_final','pedagio')
    

admin.site.register(models.Formacompanhamento,formacompanhamentoadmin)