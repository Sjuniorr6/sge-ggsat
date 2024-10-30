from django.contrib import admin

# Register your models here.
from . import models 

class requisicoesadmin(admin.ModelAdmin):
    list_display = (
    'nome',
    'endereco',
    'cnpj',
    'contrato',
    'inicio_de_contrato',
    'vigencia',
    'data',
    'motivo',
    'envio',
    'comercial',
    'tipo_produto',
    'carregador',
    'cabo',
    'tipo_fatura',
    'valor_unitario',
    'valor_total',
    'forma_pagamento',
    'observacoes',
    'TP',
    'status_faturamento',
    'id_equipamentos','numero_de_equipamentos','aos_cuidados'
)
    search_fields = ('nome',)

admin.site.register(models.Requisicoes,requisicoesadmin)