from django.db import models

# Create your models here.
from django.db import models
from acompanhamento.models import Clientes   
from produto.models import Produto    

from django.utils import timezone

class registrodemanutencao(models.Model):
    TRATATIVAS = [
        ('Oxidação', 'Oxidação'),
        ('Placa Danificada', 'Placa Danificada'),
        ('USB Danificado', 'USB Danificado'),
        ('Botão de acionamento Danificado', 'Botão de acionamento Danificado'),
        ('Antena LoRa Danificada', 'Antena LoRa Danificada'),
        ('USB Sem problemas Identificados', 'USB Sem problemas Identificados'),
    ]

    TIPO_ENVIO = [
        ('Agente', 'Agente'),
        ('Retirada', 'Retirada'),
        ('Motoboy', 'Motoboy'),
        ('Transportadora', 'Transportadora'),
        ('Correio', 'Correio'),
        ('Comercial', 'Comercial'),
    ]

    MOTIVOS = [
        ('', ''),
        ('Manutenção', 'Manutenção'),
        ('Devolução/Estoque', 'Devolução/Estoque'),
    ]

    FATURAMENTO = [
        ('', ''),
        ('Com_Custo', 'Com Custo'),
        ('Sem_Custo', 'Sem Custo'),
    ]

    STATUS_CHOICES = [
        ('Aprovado', 'Aprovado'),
        ('Reprovado pela Diretoria', 'Reprovado pela Diretoria'),
        ('Aprovado pela Diretoria', 'Aprovado pela Diretoria'),
        ('Pendente', 'Pendente'),
        ('Expedição', 'Expedição'),
        ('expedido', 'expedido'),
    ]

    ENTRADA = [
        ('Manutenção', 'Manutenção'),
        ('Devolução/Estoque', 'Devolução/Estoque'),
    ]
    SETOR = [
        ('Entrada', 'Entrada'),
        ('Manutenção', 'Manutenção'),
        ('configuração', 'configuração'),
    ]

    CUSTOMIZACOES = [
        ('', ''),
        ('Sem customização', 'Sem customização'),
        ('Caixa de papelão', 'Caixa de papelão'),
        ('Caixa de papelão (bateria desacoplada)', 'Caixa de papelão (bateria desacoplada)'),
        # Adicione o restante dos valores conforme necessário
    ]

    RECEBIMENTO_TIPO = [
        ('Correios/Transportadora', 'Correios/Transportadora'),
        ('Entrega na base', 'Entrega na base'),
        ('Motoboy', 'Motoboy'),
        
    ]
    custom= [

        ('Sem custumização' , 'Sem custumização'),
        ('Caixa de papelão' , 'Caixa de papelão' ),
        ('Caixa de papelão (bateria desacoplada)' , 'Caixa de papelão (bateria desacoplada)'),
        ('Caixa de papelão + DF' , 'Caixa de papelão + DF'),
        ('Termo branco' , 'Termo branco'),
        ('Termo branco + Imã' , 'Termo branco + Imã'),
        ('Termo branco + D.F ' , 'Termo branco + D.F'),
        ('Termo branco slim ' , 'Termo branco slim'),
        ('Termo branco slim + D.F +EQT  ' , 'Termo branco slim + D.F +EQT'),
        ('Termo cinza slim + D.F +EQT  ' , 'Termo cinza slim + D.F +EQT'),
        ('Termo branco  (isopor) ' , 'Termo branco  (isopor)'),
        ('Termo branco - bateria externa ' , 'Termo branco - bateria externa'),
        ('Termo marrom + imã' , 'Termo marrom + imã'),
        ('Termo cinza' , 'Termo cinza'),
        ('Termo cinza + imã' , 'Termo cinza + imã'),
        ('Termo preto' , 'Termo preto'),
        ('Termo preto + imã' , 'Termo preto + imã'),
        ('Termo brabco |marrim-slim' , 'Termo brabco |marrim-slim'),
        ('Termo marrom slim +D.F + EQT' , 'Termo marrom slim +D.F + EQT'),
        ('Termo marrom' , 'Termo marrom'),
        ('Caixa blindada' , 'Caixa blindada'),
        ('Tênis/ Sapato' , 'Tênis/ Sapato'),
        ('Projetor' , 'Projetor'),
        ('Caixa de som' , 'Caixa de som'),
        ('Luminaria' , 'Luminaria'),
        ('Alexa' , 'Alexa'),
        ('Video Game' , 'Video Game'),
        ('Secador de cabelo' , 'Secador de cabelo'),
        ('Roteador' , 'Roteador'),
        ('Relogio digital' , 'Relogio digital'),
    ]

    nome = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='formulario_nome')
    tipo_entrada = models.CharField(choices=ENTRADA, null=True, blank=True, max_length=50)
    tipo_produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='formulario_produto')
    motivo = models.CharField(choices=MOTIVOS, null=True, blank=True, max_length=50)
    tipo_customizacao = models.CharField(choices=CUSTOMIZACOES, null=True, blank=True, max_length=50)
    recebimento = models.CharField(choices=RECEBIMENTO_TIPO, null=True, blank=True, max_length=50)
    entregue_por_retirado_por = models.CharField(choices=RECEBIMENTO_TIPO,max_length=50, default="")
    id_equipamentos = models.TextField(max_length=1200, blank=True, default='')
    quantidade = models.TextField(max_length=50, blank=True, default='')


    
    faturamento = models.CharField(choices=FATURAMENTO, null=True, blank=True, max_length=50,default='Pendente')
    setor = models.CharField(choices=SETOR, null=True, blank=True, max_length=50)
    customizacaoo = models.CharField(choices=custom,max_length=250, blank=True, default='')
    numero_equipamento = models.TextField(max_length=2500, blank=True, default='')
    observacoes = models.TextField(max_length=250, blank=True, default='')
    tratativa = models.CharField(choices=TRATATIVAS, null=True, blank=True, max_length=50)
    imagem = models.ImageField(upload_to='imagens/', null=True, blank=True)
    imagem2 = models.ImageField(upload_to='imagens/', null=True, blank=True)
    status = models.CharField(default='Pendente', max_length=50, null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True, blank=True)
   












class ImagemRegistro(models.Model):

    SETORID = [
        ('Retorno', 'Retorno'),
        ('Manutenção', 'Manutenção'),
        
       
    ]
    TIPO_PROBLEMAS = [
        ('Oxidação', 'Oxidação'),
        ('Placa Danificada', 'Placa Danificada'),
        ('Placa danificada SEM CUSTO', 'Placa danificada SEM CUSTO'),
        ('USB Danificado', 'USB Danificado'),
        ('USB Danificado SEM CUSTO', 'USB Danificado SEM CUSTO'),
        ('Botão de acionamento Danificado', 'Botão de acionamento Danificado'),
        ('Botão de acionamento Danificado SEM CUSTO', 'Botão de acionamento Danificado SEM CUSTO'),
        ('Antena LoRa Danificada', 'Antena LoRa Danificada'),
        ('Sem problemas Identificados', 'Sem problemas Identificados'),
    ]
    tipo_problema = models.CharField(choices=TIPO_PROBLEMAS, null=True, blank=True, max_length=50)
    registro = models.ForeignKey(registrodemanutencao, related_name='imagens', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='imagens_registros/')
    imagem2 = models.ImageField(upload_to='imagens_registros/',null=True, blank=True)
    id_equipamento = models.CharField(max_length=255, blank=True)

    def __str__(self):
        
        descricao_display = f": {self.descricao}" if self.descricao else ""
        return f"Imagem ID {self.id}{descricao_display} - Registro {self.registro.id}"


class retorno(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='clientes')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='produtos')
    tipo_problema = models.CharField(max_length=100, choices=[
        ('Oxidação', 'Oxidação'),
        ('Placa Danificada', 'Placa Danificada'),
        ('Placa danificada SEM CUSTO', 'Placa danificada SEM CUSTO'),
        ('USB Danificado', 'USB Danificado'),
        ('USB Danificado SEM CUSTO', 'USB Danificado SEM CUSTO'),
        ('Botão de acionamento Danificado', 'Botão de acionamento Danificado'),
        ('Botão de acionamento Danificado SEM CUSTO', 'Botão de acionamento Danificado SEM CUSTO'),
        ('Antena LoRa Danificada', 'Antena LoRa Danificada'),
        ('Sem problemas Identificados', 'Sem problemas Identificados'),
    ])
    imagem = models.ImageField(upload_to='imagens/')
    id_equipamentos = models.TextField(max_length=1000, blank=True, default='')

    def __str__(self):
        return f"{self.cliente} - {self.produto} - {self.tipo_problema}" 