# Generated by Django 5.1.1 on 2024-10-16 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pparada', '0026_alter_paradasegura_tipo_posto'),
    ]

    operations = [
        migrations.AddField(
            model_name='paradasegura',
            name='tipo_parada',
            field=models.CharField(blank=True, choices=[('Pernoite', 'Pernoite'), ('Almoço', 'Almoço'), ('Check List', 'heck List')], max_length=255, null=True),
        ),
    ]
