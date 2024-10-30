from django import forms
from .models import paradasegura

class paradaForm(forms.ModelForm):
    class Meta:
        model = paradasegura
        fields = [
            'embarcador', 'tipo_posto','tipo_parada','nome_do_pa', 'id_rastreador', 'id_cadeado', 'transportador', 'placa_cavalo','placa_carreta',
            'nome_motorista', 'previsao_de_saida', 'Horario_de_saida',
            'inconformidade', 'descreva'
        ]
        widgets = {
            'embarcador': forms.Select(attrs={'class': 'form-control'}),
            'tipo_posto': forms.Select(attrs={'class': 'form-control'}),
            'nome_do_pa': forms.Select(attrs={'class': 'form-control'}),
            'tipo_parada': forms.Select(attrs={'class': 'form-control'}),
            'transportador': forms.TextInput(attrs={'class': 'form-control'}),
            'placa_cavalo': forms.TextInput(attrs={'class': 'form-control'}),
            'placa_carreta': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_motorista': forms.TextInput(attrs={'class': 'form-control'}),
            'previsao_de_saida': forms.TextInput(attrs={'class': 'form-control'}),
            'Horario_de_saida': forms.TextInput(attrs={'class': 'form-control'}),
            'inconformidade': forms.Select(attrs={'class': 'form-control'}),
            'descreva': forms.Textarea(attrs={'class': 'form-control'}),
            'id_rastreador': forms.Select(attrs={'class': 'form-control'}),
            'id_cadeado': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(paradaForm, self).__init__(*args, **kwargs)
        # Inicializa iscas e cadeados como escolhas vazias
        self.fields['id_rastreador'].choices = []
        self.fields['id_cadeado'].choices = []
        self.fields['nome_do_pa'].choices = []

        if self.instance and self.instance.tipo_posto:
            posto = self.instance.tipo_posto
            iscas = paradasegura.POSTOS_INFO1.get(posto, {}).get('iscas', [])
            cadeados = paradasegura.POSTOS_INFO1.get(posto, {}).get('cadeados', [])
            pa = paradasegura.POSTOS_INFO2.get(posto, {}).get('pa', [])

            # Preencher os campos com os valores das iscas, cadeados e PA
            self.fields['id_rastreador'].choices = iscas
            self.fields['id_cadeado'].choices = cadeados
            self.fields['nome_do_pa'].choices = pa


from django import forms
from .models import passagemmodel

class PassagemModelForm(forms.ModelForm):
    class Meta:
        model = passagemmodel
        fields = [
            'nome_do_posto',
            'nome_do_pa',
            'turno',
            'Iscas',
            'notebook',
            'celular',
            'antena',
            'bodycam',
            'cadeados',
            'drone',
            'descrição',
            'fotos',
        ]
        widgets = {
            'nome_do_pa': forms.Select(attrs={'class': 'form-control'}),
            'nome_do_posto': forms.Select(attrs={'class': 'form-control'}),
            'turno': forms.Select(attrs={'class': 'form-control'}),
            'Iscas': forms.Select(attrs={'class': 'form-control'}),
            'notebook': forms.Select(attrs={'class': 'form-control'}),
            'celular': forms.Select(attrs={'class': 'form-control'}),
            'antena': forms.Select(attrs={'class': 'form-control'}),
            'bodycam': forms.Select(attrs={'class': 'form-control'}),
            'cadeados': forms.Select(attrs={'class': 'form-control'}),
            'drone': forms.Select(attrs={'class': 'form-control'}),
            'descrição': forms.Select(attrs={'class': 'form-control'}),
            'fotos': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
