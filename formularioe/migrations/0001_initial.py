# Generated by Django 5.1.1 on 2024-10-02 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acompanhamento', '0001_initial'),
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='formularioe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_entrada', models.CharField(blank=True, choices=[('Manutenção', 'Manutenção'), ('Devolução/Estoque', 'Devolução/Estoque')], max_length=50, null=True)),
                ('tipo_customizacao', models.CharField(blank=True, choices=[('Sem custumização', 'Sem custumização'), ('Caixa de papelão', 'Caixa de papelão'), ('Caixa de papelão (bateria desacoplada)', 'Caixa de papelão (bateria desacoplada)'), ('Caixa de papelão + DF', 'Caixa de papelão + DF'), ('Termo branco', 'Termo branco'), ('Termo branco + D.F ', 'Termo branco + D.F'), ('Termo branco slim ', 'Termo branco slim'), ('Termo branco slim + D.F +EQT  ', 'Termo branco slim + D.F +EQT'), ('Termo cinza slim + D.F +EQT  ', 'Termo cinza slim + D.F +EQT'), ('Termo branco  (isopor) ', 'Termo branco  (isopor)'), ('Termo branco - bateria externa ', 'Termo branco - bateria externa'), ('Termo marrom + imã', 'Termo marrom + imã'), ('Termo cinza', 'Termo cinza'), ('Termo cinza + imã', 'Termo cinza + imã'), ('Termo preto', 'Termo preto'), ('Termo preto + imã', 'Termo preto + imã'), ('Termo brabco |marrim-slim', 'Termo brabco |marrim-slim'), ('Termo marrom slim +D.F + EQT', 'Termo marrom slim +D.F + EQT'), ('Termo marrom', 'Termo marrom'), ('Caixa blindada', 'Caixa blindada'), ('Tênis/ Sapato', 'Tênis/ Sapato'), ('Projetor', 'Projetor'), ('Caixa de som', 'Caixa de som'), ('Luminaria', 'Luminaria'), ('Alexa', 'Alexa'), ('Video Game', 'Video Game'), ('Secador de cabelo', 'Secador de cabelo'), ('Roteador', 'Roteador'), ('Relogio digital', 'Relogio digital')], max_length=50, null=True)),
                ('recebimento', models.CharField(blank=True, choices=[('Correios/Transportadora', 'Correios/Transportadora'), ('Entrga na base', 'Entrga na base'), ('Retirado pelo cliente', 'Retirado pelo cliente')], max_length=50, null=True)),
                ('entregue_por_retirado_por', models.CharField(max_length=100)),
                ('id_equipamentos', models.CharField(blank=True, default='', max_length=100)),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formularioe_nome', to='acompanhamento.clientes')),
                ('tipo_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formularioe_produto', to='produto.produto')),
            ],
        ),
    ]