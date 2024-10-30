from django import forms
from .models import Qualit

class QualitForm(forms.ModelForm):
    class Meta:
        model = Qualit
        fields = [
            'data', 'numero_requisicao', 'tipo_pedido', 'comercial', 'cliente', 'imei', 'id_equipamento', 'device_id', 
            'iccid_novo', 'contrato', 'modelo', 'tp', 'operadora', 'usuario','observacoes','customizacao'
        ]
        widgets = {
            'data': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_requisicao': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_pedido': forms.Select(attrs={'class': 'form-control'}),
            'comercial': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'imei': forms.TextInput(attrs={'class': 'form-control'}),
            'id_equipamento': forms.TextInput(attrs={'class': 'form-control'}),
            'device_id': forms.TextInput(attrs={'class': 'form-control'}),
            'iccid_novo': forms.TextInput(attrs={'class': 'form-control'}),
            'contrato': forms.Select(attrs={'class': 'form-control'}),
            'modelo': forms.Select(attrs={'class': 'form-control'}),
            'tp': forms.Select(attrs={'class': 'form-control'}),
            'operadora': forms.Select(attrs={'class': 'form-control'}),
            'usuario': forms.TextInput(attrs={'class': 'form-control'}),  # Campo oculto
            'observacoes': forms.TextInput(attrs={'class': 'form-control'}),
            'customizacao': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['usuario'].initial = user.id
