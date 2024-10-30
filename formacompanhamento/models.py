from django.db import models
from .models_agentes import agentes 
 # Certifique-se de que o caminho está correto

class Formacompanhamento(models.Model):
    prestador2 = [
        ("Sombra armado", "Sombra armado")
    ]

    data_inicio = models.DateTimeField(blank=True, null=True)
    data_final = models.DateTimeField(blank=True, null=True)
    prestador = models.CharField(choices=prestador2, max_length=50, null=False, blank=False)
    agente = models.ForeignKey(agentes, on_delete=models.CASCADE)  # Usando 'agentes' com a primeira letra minúscula
    placa = models.CharField(max_length=255)
    id_equipamento = models.CharField(max_length=255)
    km_inicial = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    km_final = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    pedagio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, null=True,blank=True, default='Pendente')

    def __str__(self):
        return self.placa


