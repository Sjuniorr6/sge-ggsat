from django.contrib import admin
from .models import Qualit

class QualitAdmin(admin.ModelAdmin):
    list_display = [
        'data', 'numero_requisicao', 'tipo_pedido', 'comercial', 'cliente', 'imei', 'id_equipamento', 'device_id', 
        'iccid_novo', 'contrato', 'modelo', 'tp', 'operadora', 'usuario','observacoes' ,'customizacao'
    ]

admin.site.register(Qualit, QualitAdmin)
