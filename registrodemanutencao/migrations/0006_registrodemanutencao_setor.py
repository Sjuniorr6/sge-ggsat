# Generated by Django 5.1.1 on 2024-10-15 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrodemanutencao', '0005_remove_registrodemanutencao_setor'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrodemanutencao',
            name='setor',
            field=models.CharField(blank=True, choices=[('Entrada', 'Entrada'), ('Manutenção', 'Manutenção'), ('configuração', 'configuração')], max_length=50, null=True),
        ),
    ]