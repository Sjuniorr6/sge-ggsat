# Generated by Django 5.1.1 on 2024-10-07 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reativacao', '0008_alter_reativacao_motivo_reativacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reativacao',
            name='motivo_reativacao',
            field=models.CharField(blank=True, choices=[('Retornavel', 'Retornavel'), ('Descartavel', 'Descartavel')], max_length=50, null=True),
        ),
    ]