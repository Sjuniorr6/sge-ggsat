# Generated by Django 5.1.1 on 2024-10-02 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reativacao', '0002_alter_reativacao_status_reativacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reativacao',
            name='status_reativacao',
            field=models.CharField(choices=[('Faturado', 'Faturado'), ('Pendente', 'Pendente')], default='', max_length=20),
        ),
    ]
