from django.db import models

class Clientes(models.Model):




    vigencia_tipo = [

        ('N/A' , 'N/A'),
        ('12' , '12'),
        ('24' , '24' ),
        ('36' , '36'),
        ('48' , '48'),
    ]
    status = [

        ('Ativo' , 'Ativo'),
        ('Inativo' , 'Inativo'),

    ]
    equipamentos = [

        ("Isaca","Isca"),
        ("Rastreador","Rastreador"),
        ("Tets","Tets"),
    ]
    contratos = [

        ("",""),
        ("Descartavel","Descartavel"),
        ("Retornavel","Retornavel"),
        
    ]

    nome = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100, null=True)
    endereco = models.CharField(max_length=255)


    cnpj = models.CharField(max_length=20)

    

    tipo_contrato = models.CharField(choices=contratos, max_length=50, null=True,blank=True)
    inicio_de_contrato = models.DateField(null=True, blank=True)
    
    vigencia = models.CharField(choices=vigencia_tipo ,null=True,blank=True, max_length=50)
    status = models.CharField(choices=status ,null=True,blank=True, max_length=50)
    termino = models.CharField(max_length=10,null=True,blank=True)
    equipamento = models.CharField(choices=equipamentos, max_length= 50, null=True, blank=False )
    quantidade = models.IntegerField(null=True, blank=True)
    gr = models.CharField(null=True, blank=True,max_length=50)
    corretora = models.CharField(null=True, blank=True,max_length=50)
    seguradora = models.CharField(null=True, blank=True,max_length=50)

    def __str__(self):
        return self.nome