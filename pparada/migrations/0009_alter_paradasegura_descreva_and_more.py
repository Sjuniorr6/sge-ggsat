# Generated by Django 5.1.1 on 2024-10-14 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pparada', '0008_alter_paradasegura_id_cadeado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paradasegura',
            name='descreva',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paradasegura',
            name='id_cadeado',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paradasegura',
            name='id_rastreador',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paradasegura',
            name='inconformidade',
            field=models.CharField(blank=True, choices=[('NÃO', 'NÃO'), ('SENSOR PORTA MOTORISTA', 'SENSOR PORTA MOTORISTA'), ('SENSOR PORTA PASSAGEIRO', 'SENSOR PORTA PASSAGEIRO'), ('TECLADO', 'TECLADO'), ('BOTÃO DE PÂNICO', 'BOTÃO DE PÂNICO'), ('LACRE BAÚ', 'LACRE BAÚ'), ('SIRENE', 'SIRENE'), ('BLOQUEIO', 'BLOQUEIO'), ('CHAVE GERAL', 'CHAVE GERAL'), ('CNH', 'CNH'), ('DOCUMENTO DO VEÍCULO', 'DOCUMENTO DO VEÍCULO'), ('DOCUMENTO DA CARRETA', 'DOCUMENTO DA CARRETA'), ('OUTROS', 'OUTROS')], max_length=255, null=True),
        ),
    ]
