# Generated by Django 5.1.1 on 2024-10-02 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nome_fantasia', models.CharField(max_length=100, null=True)),
                ('endereco', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=20)),
                ('tipo_contrato', models.CharField(blank=True, choices=[('', ''), ('Descartavel', 'Descartavel'), ('Retornavel', 'Retornavel')], max_length=50, null=True)),
                ('inicio_de_contrato', models.DateField()),
                ('vigencia', models.CharField(blank=True, choices=[('', ''), ('12', '12'), ('24', '24'), ('36', '36'), ('48', '48')], max_length=50, null=True)),
                ('status', models.CharField(blank=True, choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], max_length=50, null=True)),
                ('termino', models.CharField(blank=True, max_length=10, null=True)),
                ('equipamento', models.CharField(choices=[('Isaca', 'Isca'), ('Rastreador', 'Rastreador'), ('Tets', 'Tets')], max_length=50, null=True)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('gr', models.CharField(blank=True, max_length=50, null=True)),
                ('corretora', models.CharField(blank=True, max_length=50, null=True)),
                ('transportadora', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]