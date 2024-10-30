# Generated by Django 5.1.1 on 2024-10-02 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qualit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=50, null=True)),
                ('numero_requisicao', models.CharField(max_length=50)),
                ('tipo_pedido', models.CharField(blank=True, choices=[('Tipo de Faturamento', 'Tipo de Faturamento'), ('Aquisicão Nova', 'Aquisicão Nova'), ('Manutenção', 'Manutenção'), ('Aditivo', 'Aditivo'), ('Acessorios', 'Acessorios'), ('Extravio', 'Extravio'), ('Texte', 'Texte'), ('Isca Fast', 'Isca Fast'), ('Isca Fast Agente', 'Isca Fast Agente'), ('Antenista', 'Antenista'), ('Reversa', 'Reversa')], max_length=100, null=True)),
                ('comercial', models.CharField(max_length=100, null=True)),
                ('cliente', models.CharField(max_length=100, null=True)),
                ('imei', models.CharField(max_length=50)),
                ('id_equipamento', models.CharField(max_length=50)),
                ('device_id', models.CharField(max_length=50)),
                ('iccid_novo', models.CharField(max_length=50)),
                ('contrato', models.CharField(blank=True, choices=[('', ''), ('Descartavel', 'Descartavel'), ('Retornavel', 'Retornavel')], max_length=50, null=True)),
                ('modelo', models.CharField(max_length=100, null=True)),
                ('tp', models.CharField(blank=True, choices=[('5', '5'), ('10', '10'), ('15', '15'), ('30', '30'), ('60', '60'), ('360', '360'), ('720', '720')], max_length=50, null=True)),
                ('operadora', models.CharField(choices=[('ESEYE', 'ESEYE'), ('1NCE', '1NCE')], max_length=100)),
                ('usuario', models.CharField(max_length=50, null=True)),
                ('observacoes', models.CharField(max_length=50, null=True)),
                ('customizacao', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
