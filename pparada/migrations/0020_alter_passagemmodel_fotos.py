# Generated by Django 5.1.1 on 2024-10-15 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pparada', '0019_passagemmodel_turno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passagemmodel',
            name='fotos',
            field=models.ImageField(blank=True, choices=[('Não Confome', 'Não Confome'), ('Confome', 'Confome')], max_length=255, null=True, upload_to=''),
        ),
    ]
