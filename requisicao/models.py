from django.db import models
from acompanhamento.models import Clientes   
from produto.models import Produto    
from django.utils import timezone
class Requisicoes(models.Model):
    # Definição das escolhas de status
    statuschoice = [
        ('Aprovado', 'Aprovado'),
        ('Reprovado', 'Reprovado'),
        ('Pendente', 'Pendente'),
        ('Configurado', 'Configurado'),
        ('Expedido', 'Expedido'),
    ]

    # Definição das escolhas de TP (tempo de processamento)
    TP = [
        ('5', '5'),
        ('10', '10'),
        ('15', '15'),
        ('30', '30'),
        ('60', '60'),
        ('360', '360'),
        ('720', '720'),
    ]
    statusfat = [
        
        
        
        ('Pendente', 'Pendente'),
        ('Faturado sem taxa', 'Faturado sem taxa'),
        ('Faturado com taxa', 'Faturado com taxa'),
        ('Pendente', 'Pendente'),
        ('Pendente sem Contrato', 'Pendente sem Contrato'),
        ('Pendente Sem Termo', 'Pendente Sem Termo'),
        ('Pendente Sem Contrato', 'Pendente Sem Contrato'),
        ('Sem Custo', 'Sem Custo'),
        ('Dados invalidos', 'Dados invalidos'),
    ]
    motivoc = [
        ('Tipo de Faturamento', 'Tipo de Faturamento'),
        ('Aquisicão Nova', 'Aquisicão Nova'),
        ('Manutenção', 'Manutenção'),
        ('Aditivo', 'Aditivo'),
        ('Acessórios', 'Acessórios'),
        ('Extravio', 'Extravio'),
        ('Teste', 'Teste'),
        
        ('Isca Fast - Agente', 'Isca Fast - Agente'),
        ('Antenista', 'Antenista'),
        ('Reversa', 'Reversa'),
        ('Isca FAST', 'Isca FAST'),
        ('Estoque Antenista', 'Estoque Antenista'),
        ('Renovação', 'Renovação'),
    ]


    # Definição das escolhas de tipo de envio
    tipo_envio = [
        ('Agente', 'Agente'),
        ('Retirada na base', 'Retirada na base'),
        ('Motoboy', 'Motoboy'),
        ('transportadora', 'Transportadora'),
        ('Correio', 'Correio'),
        ('Comercial', 'Comercial'),
    ]

    # Definição das escolhas de tipo de contrato
    contrato_tipo = [
        ('', ''),
        ('Descartavel', 'Descartavel'),
        ('Retornavel', 'Retornavel'),
    ]

    # Definição das escolhas de tipo de fatura
    fatura_tipo = [
        ('Com Custo', 'Com Custo'),
        ('Sem Custo', 'Sem Custo'),
    ]

    # Definição das escolhas de status
    STATUS_CHOICES = [
        ('Aprovado', 'Aprovado'),
        ('Reprovado', 'Reprovado'),
        ('Pendente', 'Pendente'),
        ('Configurado', 'Configurado'),
        ('Reprovado pelo CEO', 'Reprovado pelo CEO'),
        ('Aprovado pelo CEO', 'Aprovado pelo CEO'),
        ('Reprovado pela Diretoria', 'Reprovado pela Diretoria'),
        ('Aprovado pela Diretoria', 'Aprovado pela Diretoria'),
        ('Pedido para o cliente', 'Pedido para o cliente'),
    ]
    customizacoes = [

        ('Sem custumização' , 'Sem custumização'),
        ('Caixa de papelão' , 'Caixa de papelão' ),
        ('Caixa de papelão (bateria desacoplada)' , 'Caixa de papelão (bateria desacoplada)'),
        ('Caixa de papelão + DF' , 'Caixa de papelão + DF'),
        ('Termo branco' , 'Termo branco'),
        ('Termo branco + imã' , 'Termo branco + imã'),
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
        ('Termo branco - slim' , 'Termo branco - slim'),
        ('Termo marrom slim +D.F + EQT' , 'Termo marrom slim +D.F + EQT'),
        ('Termo marrom' , 'Termo marrom'),
        ('Termo marrom + ETQ' , 'Termo marrom + ETQ'),
        ('Termo marrom slim' , 'Termo marrom slim'),
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
    meses = [
    ('N/A', 'N/A'),
    ('6', '6'),
    ('12', '12'),
    ('18', '18'),
    ('24', '24'),
    ('30', '30'),
    ('36', '36'),
    ('48', '48'),
]
    ANTENISTA_CHOICES = [
    ('RODRIGO SILVA', 'RODRIGO SILVA'),
    ('FELIPPE CAMELO', 'FELIPPE CAMELO'),
    ('FILIPPE CAMELO', 'FILIPPE CAMELO'),
    ('JOSÉ ANTONIO', 'JOSÉ ANTONIO'),
    ('CESAR RODRIGO - SPO', 'CESAR RODRIGO - SPO'),
    ('LUCIO', 'LUCIO'),
    ('FELIPE MACEDO - SPO', 'FELIPE MACEDO - SPO'),
    ('RAFAEL ALVES - SPO', 'RAFAEL ALVES - SPO'),
    ('ANDERSON COSTA / L', 'ANDERSON COSTA / L'),
    ('YURI NETTO', 'YURI NETTO'),
    ('HERCULES / FILIPE', 'HERCULES / FILIPE'),
    ('ALEXANDRE', 'ALEXANDRE'),
    ('AILTON', 'AILTON'),
    ('SATURNINO', 'SATURNINO'),
    ('CLEBSON ARANDU - SPO', 'CLEBSON ARANDU - SPO'),
    ('TENORIO', 'TENORIO'),
    ('WILSON JOSE', 'WILSON JOSE'),
    ('WESLEY RODRIGO', 'WESLEY RODRIGO'),
    ('WESLEY RODRIGO - SPO', 'WESLEY RODRIGO - SPO'),
    ('ANGELO/AGATHA', 'ANGELO/AGATHA'),
    ('STEVERSON ROGGER', 'STEVERSON ROGGER'),
    ('IGOR BARBOSA', 'IGOR BARBOSA'),
    ('CAIQUE GONÇALVES', 'CAIQUE GONÇALVES'),
    ('GIOVAN MENDES', 'GIOVAN MENDES'),
    ('RONALDO/SILVA', 'RONALDO/SILVA'),
    ('CARDOSO/PAULA', 'CARDOSO/PAULA'),
    ('BORGES / ALMEIDA - JONAS', 'BORGES / ALMEIDA - JONAS'),
    ('DINAYDER/CLEITON - JONAS', 'DINAYDER/CLEITON - JONAS'),
    ('IVAN/LEANDRO - ALEX', 'IVAN/LEANDRO - ALEX'),
    ('WILSON JOSE - SPO', 'WILSON JOSE - SPO'),
    ('VINICIUS SUHE', 'VINICIUS SUHE'),
    ('AURELIO ANDRADE - RJ', 'AURELIO ANDRADE - RJ'),
    ('THAISY/JOAO PEDRO', 'THAISY/JOAO PEDRO'),
    ('PAULO VICENTE/LUCIA - JONAS', 'PAULO VICENTE/LUCIA - JONAS'),
    ('ANDERSON NOGUEIRA', 'ANDERSON NOGUEIRA'),
    ('THIAGO MATHEUS - SPO', 'THIAGO MATHEUS - SPO'),
    ('SIMEI SANTANA - SPO', 'SIMEI SANTANA - SPO'),
    ('FLORIANO FERREIRA - SPO', 'FLORIANO FERREIRA - SPO'),
    ('AURELIO', 'AURELIO'),
    ('RAPHAEL/LIMA', 'RAPHAEL/LIMA'),
    ('RIBEIRO/DUTRA', 'RIBEIRO/DUTRA'),
    ('HUGO/MOTTA', 'HUGO/MOTTA'),
    ('ANDRADE/LEONARDO', 'ANDRADE/LEONARDO'),
    ('ANDERSON/MARCIO', 'ANDERSON/MARCIO'),
    ('SILVIO ROMERO', 'SILVIO ROMERO'),
    ('ALEX SILVA', 'ALEX SILVA'),
    ('GABRIEL QUILANTE', 'GABRIEL QUILANTE'),
    ('VITOR ROGERIO', 'VITOR ROGERIO'),
    ('MARCIO JUNIOR', 'MARCIO JUNIOR'),
    ('TADEU', 'TADEU'),
    ('LEANDRO FERREIRA - RJ', 'LEANDRO FERREIRA - RJ'),
    ('NASCIMENTO/AMERSON', 'NASCIMENTO/AMERSON'),
    ('IZABEL/SAMPAIO', 'IZABEL/SAMPAIO'),
    ('ANDRE/TELES', 'ANDRE/TELES'),
    ('ALLAN/CRISTINA', 'ALLAN/CRISTINA'),
    ('CARLOS MAIA/FELIPE SOUSA', 'CARLOS MAIA/FELIPE SOUSA'),
    ('FELIPE SOUZA', 'FELIPE SOUZA'),
    ('ROBSON RAMIRO', 'ROBSON RAMIRO'),
    ('WASHINGTON FERNANDES - RJ', 'WASHINGTON FERNANDES - RJ'),
    ('CARLOS CARVALHO/DIOGO SENA', 'CARLOS CARVALHO/DIOGO SENA'),
    ('ROGERIO/ISMAEL', 'ROGERIO/ISMAEL'),
    ('JANDERSO FERNANDES', 'JANDERSO FERNANDES'),
    ('JOAO MARCOS', 'JOAO MARCOS'),
    ('ADRIANO GONÇALVES', 'ADRIANO GONÇALVES'),
    ('COUTINHO/SANTOS', 'COUTINHO/SANTOS'),
    ('NUNES/CRYSOSTOMO', 'NUNES/CRYSOSTOMO'),
    ('ESTEVAO/ULYSSES', 'ESTEVAO/ULYSSES'),
    ('ALCIDES', 'ALCIDES'),
    ('EZEQUIEL', 'EZEQUIEL'),
    ('NILDO', 'NILDO'),
    ('ALEX', 'ALEX'),
    ('ANDERSON', 'ANDERSON'),
    ('ANTONIEQUE', 'ANTONIEQUE'),
    ('OSNI', 'OSNI'),
    ('ELTON', 'ELTON'),
    ('NEY', 'NEY'),
    ('ANDRÉ', 'ANDRÉ'),
    ('RILDO', 'RILDO'),
    ('WELLINGTHON', 'WELLINGTHON'),
    ('GERSON WALACE', 'GERSON WALACE'),
    ('JUSTINO', 'JUSTINO'),
    ('ANTONIO', 'ANTONIO'),
    ('FRANCISCO', 'FRANCISCO'),
    ('OSMAN', 'OSMAN'),
    ('TONHARA', 'TONHARA'),
    ('EMERSON', 'EMERSON'),
    ('MARCELO', 'MARCELO'),
    ('JEFFERSON', 'JEFFERSON'),
    ('GUILHERME', 'GUILHERME'),
    ('MARCIO', 'MARCIO'),
    ('SAMPAIO', 'SAMPAIO'),
    ('DIOGO', 'DIOGO'),
    ('WESLEY', 'WESLEY'),
    ('EVERALDO / SAMUEL', 'EVERALDO / SAMUEL'),
    ('ERIK', 'ERIK'),
    ('LUCAS CARVALHO', 'LUCAS CARVALHO'),
    ('RODRIGO', 'RODRIGO'),
    ('PITTA', 'PITTA'),
    ('JUSTO', 'JUSTO'),
    ('PAULO HENRIQUE', 'PAULO HENRIQUE'),
    ('EDUARDO', 'EDUARDO'),
    ('YURI', 'YURI'),
    ('RAFAEL', 'RAFAEL'),
    ('MARLON', 'MARLON'),
    ('MALLONE ROCHA DA SILVA', 'MALLONE ROCHA DA SILVA'),
    ('Ian Carlos Severino', 'Ian Carlos Severino'),
    ('Matheus (Praia Grande)', 'Matheus (Praia Grande)'),
    ('André Tsubamoto | Uniforme Seguros', 'André Tsubamoto | Uniforme Seguros'),
    ('Fernandes - Nordeste Seguros', 'Fernandes - Nordeste Seguros'),
]
    comercial_choices = [

        ('MAYRA','MAYRA'),
        ('DANIEL','DANIEL'),
        ('MARCIO','MARCIO'),
        ('CIDO','CIDO'),
        ('ALISON','ALISON'),
        ('THIAGO','THIAGO'),
        ('GOLDEN','GOLDEN'),

    ]

    # Campos do modelo
    id = models.AutoField(primary_key=True)
    nome = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='requisicoes_nome')
    endereco = models.CharField(max_length=255, blank=True, null=True)
    contrato = models.CharField(choices=contrato_tipo, null=True, blank=True, max_length=50)
    cnpj = models.CharField(max_length=25, blank=True, null=True)
    numero_de_equipamentos = models.CharField(max_length=14, blank=True, null=True)
    inicio_de_contrato = models.DateField(blank=True, null=True)
    vigencia = models.CharField(max_length=50,choices=meses,blank=True, null=True)
    customizacao = models.CharField(max_length=50,choices=meses,blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(default=timezone.now)
    tipo_customizacao = models.CharField(choices=customizacoes ,null=True,blank=True, max_length=50)
    antenista = models.CharField(choices= ANTENISTA_CHOICES,max_length=50, blank=True, null=True)  # Novo campo para antenistas
    envio = models.CharField(choices=tipo_envio, null=True, blank=True, max_length=50)
    taxa_envio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    comercial = models.CharField(choices=comercial_choices ,max_length=100, blank=True, default='')
    tipo_produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='requisicoes_produto')
    carregador = models.CharField(max_length=100, blank=True, default='')
    motivo = models.CharField(choices=motivoc,  default='', null=True, blank=True, max_length=50)
    cabo = models.CharField(max_length=100, blank=True, default='')
    tipo_fatura = models.CharField(choices=fatura_tipo, null=True, blank=True, max_length=50)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    forma_pagamento = models.CharField(max_length=100,null=True, blank=True, default='')
    observacoes = models.TextField(max_length=250,null=True, blank=True, default='')
    aos_cuidados = models.TextField(max_length=250,null=True, blank=True, default='')
    status = models.CharField(default='Pendente', null=True, blank=True, max_length=50)
    TP = models.CharField(choices=TP, null=True, blank=True, max_length=50)
    status_faturamento = models.CharField(choices=statusfat,  default="Pendente",null=True, blank=True, max_length=50)
    id_equipamentos= models.TextField(max_length=180000, null=True, blank=True, default='')
    faturamento= models.CharField(choices=statusfat ,max_length=1200, blank=True, default='Pendente')
    def __str__(self):
        return f"Requisição {self.id} - {self.nome} "






class estoque_antenista(models.Model):
    ANTENISTA_CHOICES =[
    ('RODRIGO SILVA', 'RODRIGO SILVA'),
    ('FELIPPE CAMELO', 'FELIPPE CAMELO'),
    ('FILIPPE CAMELO', 'FILIPPE CAMELO'),
    ('JOSÉ ANTONIO', 'JOSÉ ANTONIO'),
    ('CESAR RODRIGO - SPO', 'CESAR RODRIGO - SPO'),
    ('LUCIO', 'LUCIO'),
    ('FELIPE MACEDO - SPO', 'FELIPE MACEDO - SPO'),
    ('RAFAEL ALVES - SPO', 'RAFAEL ALVES - SPO'),
    ('ANDERSON COSTA / L', 'ANDERSON COSTA / L'),
    ('YURI NETTO', 'YURI NETTO'),
    ('HERCULES / FILIPE', 'HERCULES / FILIPE'),
    ('ALEXANDRE', 'ALEXANDRE'),
    ('AILTON', 'AILTON'),
    ('SATURNINO', 'SATURNINO'),
    ('CLEBSON ARANDU - SPO', 'CLEBSON ARANDU - SPO'),
    ('TENORIO', 'TENORIO'),
    ('WILSON JOSE', 'WILSON JOSE'),
    ('WESLEY RODRIGO', 'WESLEY RODRIGO'),
    ('WESLEY RODRIGO - SPO', 'WESLEY RODRIGO - SPO'),
    ('ANGELO/AGATHA', 'ANGELO/AGATHA'),
    ('STEVERSON ROGGER', 'STEVERSON ROGGER'),
    ('IGOR BARBOSA', 'IGOR BARBOSA'),
    ('CAIQUE GONÇALVES', 'CAIQUE GONÇALVES'),
    ('GIOVAN MENDES', 'GIOVAN MENDES'),
    ('RONALDO/SILVA', 'RONALDO/SILVA'),
    ('CARDOSO/PAULA', 'CARDOSO/PAULA'),
    ('BORGES / ALMEIDA - JONAS', 'BORGES / ALMEIDA - JONAS'),
    ('DINAYDER/CLEITON - JONAS', 'DINAYDER/CLEITON - JONAS'),
    ('IVAN/LEANDRO - ALEX', 'IVAN/LEANDRO - ALEX'),
    ('WILSON JOSE - SPO', 'WILSON JOSE - SPO'),
    ('VINICIUS SUHE', 'VINICIUS SUHE'),
    ('AURELIO ANDRADE - RJ', 'AURELIO ANDRADE - RJ'),
    ('THAISY/JOAO PEDRO', 'THAISY/JOAO PEDRO'),
    ('PAULO VICENTE/LUCIA - JONAS', 'PAULO VICENTE/LUCIA - JONAS'),
    ('ANDERSON NOGUEIRA', 'ANDERSON NOGUEIRA'),
    ('THIAGO MATHEUS - SPO', 'THIAGO MATHEUS - SPO'),
    ('SIMEI SANTANA - SPO', 'SIMEI SANTANA - SPO'),
    ('FLORIANO FERREIRA - SPO', 'FLORIANO FERREIRA - SPO'),
    ('AURELIO', 'AURELIO'),
    ('RAPHAEL/LIMA', 'RAPHAEL/LIMA'),
    ('RIBEIRO/DUTRA', 'RIBEIRO/DUTRA'),
    ('HUGO/MOTTA', 'HUGO/MOTTA'),
    ('ANDRADE/LEONARDO', 'ANDRADE/LEONARDO'),
    ('ANDERSON/MARCIO', 'ANDERSON/MARCIO'),
    ('SILVIO ROMERO', 'SILVIO ROMERO'),
    ('ALEX SILVA', 'ALEX SILVA'),
    ('GABRIEL QUILANTE', 'GABRIEL QUILANTE'),
    ('VITOR ROGERIO', 'VITOR ROGERIO'),
    ('MARCIO JUNIOR', 'MARCIO JUNIOR'),
    ('TADEU', 'TADEU'),
    ('LEANDRO FERREIRA - RJ', 'LEANDRO FERREIRA - RJ'),
    ('NASCIMENTO/AMERSON', 'NASCIMENTO/AMERSON'),
    ('IZABEL/SAMPAIO', 'IZABEL/SAMPAIO'),
    ('ANDRE/TELES', 'ANDRE/TELES'),
    ('ALLAN/CRISTINA', 'ALLAN/CRISTINA'),
    ('CARLOS MAIA/FELIPE SOUSA', 'CARLOS MAIA/FELIPE SOUSA'),
    ('FELIPE SOUZA', 'FELIPE SOUZA'),
    ('ROBSON RAMIRO', 'ROBSON RAMIRO'),
    ('WASHINGTON FERNANDES - RJ', 'WASHINGTON FERNANDES - RJ'),
    ('CARLOS CARVALHO/DIOGO SENA', 'CARLOS CARVALHO/DIOGO SENA'),
    ('ROGERIO/ISMAEL', 'ROGERIO/ISMAEL'),
    ('JANDERSO FERNANDES', 'JANDERSO FERNANDES'),
    ('JOAO MARCOS', 'JOAO MARCOS'),
    ('ADRIANO GONÇALVES', 'ADRIANO GONÇALVES'),
    ('COUTINHO/SANTOS', 'COUTINHO/SANTOS'),
    ('NUNES/CRYSOSTOMO', 'NUNES/CRYSOSTOMO'),
    ('ESTEVAO/ULYSSES', 'ESTEVAO/ULYSSES'),
    ('ALCIDES', 'ALCIDES'),
    ('EZEQUIEL', 'EZEQUIEL'),
    ('NILDO', 'NILDO'),
    ('ALEX', 'ALEX'),
    ('ANDERSON', 'ANDERSON'),
    ('ANTONIEQUE', 'ANTONIEQUE'),
    ('OSNI', 'OSNI'),
    ('ELTON', 'ELTON'),
    ('NEY', 'NEY'),
    ('ANDRÉ', 'ANDRÉ'),
    ('RILDO', 'RILDO'),
    ('WELLINGTHON', 'WELLINGTHON'),
    ('GERSON WALACE', 'GERSON WALACE'),
    ('JUSTINO', 'JUSTINO'),
    ('ANTONIO', 'ANTONIO'),
    ('FRANCISCO', 'FRANCISCO'),
    ('OSMAN', 'OSMAN'),
    ('TONHARA', 'TONHARA'),
    ('EMERSON', 'EMERSON'),
    ('MARCELO', 'MARCELO'),
    ('JEFFERSON', 'JEFFERSON'),
    ('GUILHERME', 'GUILHERME'),
    ('MARCIO', 'MARCIO'),
    ('SAMPAIO', 'SAMPAIO'),
    ('DIOGO', 'DIOGO'),
    ('WESLEY', 'WESLEY'),
    ('EVERALDO / SAMUEL', 'EVERALDO / SAMUEL'),
    ('ERIK', 'ERIK'),
    ('LUCAS CARVALHO', 'LUCAS CARVALHO'),
    ('RODRIGO', 'RODRIGO'),
    ('PITTA', 'PITTA'),
    ('JUSTO', 'JUSTO'),
    ('PAULO HENRIQUE', 'PAULO HENRIQUE'),
    ('EDUARDO', 'EDUARDO'),
    ('YURI', 'YURI'),
    ('RAFAEL', 'RAFAEL'),
    ('MARLON', 'MARLON'),
    ('MALLONE ROCHA DA SILVA', 'MALLONE ROCHA DA SILVA'),
    ('Ian Carlos Severino', 'Ian Carlos Severino'),

]

    nome = models.CharField(max_length=50, choices=ANTENISTA_CHOICES)
    tipo_produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='antenista_produto')
    endereco = models.CharField(max_length=255, blank=True, null=True)
    quantidade = models.IntegerField(null=True, blank=True)
    

    def __str__(self):
        return f"{self.nome} - {self.tipo_produto}"

    def save(self, *args, **kwargs):
        print(f"Salvando estoque: {self.nome} - {self.tipo_produto} com quantidade: {self.quantidade}")
        super().save(*args, **kwargs)