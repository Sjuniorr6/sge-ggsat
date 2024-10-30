from django.db import models
from acompanhamento.models import Clientes

class Reativacao(models.Model):
    STATUS_CHOICES = [
        
        ('Faturado', 'Faturado'),
        ('Não Faturado', 'Não Faturado'),
    ]
    MOTIVO_CHOICES = [
        
        ('Retornavel', 'Retornavel'),
        ('Descartavel', 'Descartavel'),
    ]

    nome = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='reativacao_nome')
    motivo_reativacao = models.CharField(choices=MOTIVO_CHOICES,max_length=50,null=True, blank=True)
    canal_solicitacao = models.CharField(max_length=100, null=True, blank=True)
    observacoes = models.CharField(max_length=100)
    status_reativacao = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Não Faturado')
    

    def __str__(self):
        return f"Reativacao {self.id} - {self.nome}"
class IdIccid(models.Model):
    reativacao = models.ForeignKey(Reativacao, on_delete=models.CASCADE, related_name='id_iccids')
    id_equipamentos = models.CharField(max_length=300, blank=True, default='')
    ccid_equipamentos = models.CharField(max_length=300, blank=True, default='')
    quantidade = models.PositiveIntegerField(default=0)  # Campo para armazenar a quantidade

    def __str__(self):
        return f"IdIccid {self.id} - ID: {self.id_equipamentos}, ICCID: {self.ccid_equipamentos}, Quantidade: {self.quantidade}"
