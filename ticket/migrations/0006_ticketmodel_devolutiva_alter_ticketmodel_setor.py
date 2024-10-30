# Generated by Django 5.1.1 on 2024-10-21 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_remove_ticketmodel_nome_ticketmodel_usuario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketmodel',
            name='devolutiva',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticketmodel',
            name='setor',
            field=models.CharField(blank=True, choices=[('Diretoria', 'Diretoria'), ('Inteligência', 'Inteligência'), ('Faturamento', 'Faturamento'), ('Expedição', 'Expedição'), ('Configuração', 'Configuração'), ('Quality', 'Quality'), ('Área Técnica', 'Área Técnica'), ('Comercial', 'Comercial')], max_length=255, null=True),
        ),
    ]