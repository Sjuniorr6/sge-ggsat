from django.db import models
from django.contrib.auth.models import User
from acompanhamento.models import Clientes   
from produto.models import Produto 

class Qualit(models.Model):
    TIPO_PEDIDO_CHOICES = [
        ('Tipo de Faturamento', 'Tipo de Faturamento'),
        ('Aquisicão Nova', 'Aquisicão Nova'),
        ('Manutenção', 'Manutenção'),
        ('Aditivo', 'Aditivo'),
        ('Acessorios', 'Acessorios'),
        ('Extravio', 'Extravio'),
        ('Texte', 'Texte'),
        ('Isca Fast', 'Isca Fast'),
        ('Isca Fast Agente', 'Isca Fast Agente'),
        ('Antenista', 'Antenista'),
        ('Reversa', 'Reversa'),
    ]
    CONTRATO_TIPO_CHOICES = [
        ('', ''),
        ('Descartavel', 'Descartavel'),
        ('Retornavel', 'Retornavel'),
    ]
    TP_CHOICES = [
        ('5', '5'),
        ('10', '10'),
        ('15', '15'),
        ('30', '30'),
        ('60', '60'),
        ('360', '360'),
        ('720', '720'),
    ]
    OPERADORA_CHOICES = [
        ('ESEYE', 'ESEYE'),
        ('1NCE', '1NCE'),
    ]

    data = models.CharField(max_length=50, null=True)
    numero_requisicao = models.CharField(max_length=50)
    tipo_pedido = models.CharField(choices=TIPO_PEDIDO_CHOICES, max_length=100, null=True, blank=True)
    comercial = models.CharField(max_length=100, null=True)
    cliente = models.CharField(max_length=100, null=True)
    imei = models.CharField(max_length=50)
    id_equipamento = models.CharField(max_length=50)
    device_id = models.CharField(max_length=50)
    iccid_novo = models.CharField(max_length=50)
    contrato = models.CharField(choices=CONTRATO_TIPO_CHOICES, null=True, blank=True, max_length=50)
    modelo = models.CharField(max_length=100, null=True)
    tp = models.CharField(choices=TP_CHOICES, null=True, blank=True, max_length=50)
    operadora = models.CharField(choices=OPERADORA_CHOICES, max_length=100)
    usuario = models.CharField(max_length=50 ,null=True) # Atualize para um usuário válido
    observacoes = models.CharField(max_length=50 ,null=True)
    customizacao = models.CharField(max_length=50 ,null=True)


    def __str__(self):
        return self.numero_requisicao
