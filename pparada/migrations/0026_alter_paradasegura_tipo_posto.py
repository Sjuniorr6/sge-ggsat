# Generated by Django 5.1.1 on 2024-10-15 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pparada', '0025_alter_paradasegura_tipo_posto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paradasegura',
            name='tipo_posto',
            field=models.CharField(blank=True, choices=[('0', '---'), ('1', 'POSTO DA SERRA'), ('2', 'POSTO BURITIZINHO'), ('3', 'POSTO BRASILEIRÃO'), ('4', 'POSTO TREVÃO'), ('5', 'POSTO JN'), ('6', 'POSTO CAPIXABOM'), ('7', 'POSTO GRAAL RUBI')], max_length=255, null=True),
        ),
    ]
