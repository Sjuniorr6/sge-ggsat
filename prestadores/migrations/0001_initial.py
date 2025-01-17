# Generated by Django 5.1.1 on 2024-10-02 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prestador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, null=True)),
                ('franquia_km', models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=10, null=True)),
                ('franquiah', models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=10, null=True)),
                ('valor_acionamento', models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=10, null=True)),
                ('valorkm', models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=10, null=True)),
                ('valor_exedente', models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=10, null=True)),
            ],
        ),
    ]
