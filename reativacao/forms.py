from django import forms
from django.forms import inlineformset_factory
from .models import IdIccid, Reativacao

class ReativacaoForm(forms.ModelForm):
    class Meta:
        model = Reativacao
        fields = ['nome', 'motivo_reativacao', 'canal_solicitacao', 'observacoes', 'status_reativacao']
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-control'}),
            'motivo_reativacao': forms.Select(attrs={'class': 'form-control'}),
            'canal_solicitacao': forms.TextInput(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control'}),
            'status_reativacao': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ReativacaoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class IdIccidForm(forms.ModelForm):
    class Meta:
        model = IdIccid
        fields = ['id_equipamentos', 'ccid_equipamentos']
        widgets = {
            'id_equipamentos': forms.TextInput(attrs={'class': 'form-control'}),
            'ccid_equipamentos': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(IdIccidForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

IdIccidFormSet = inlineformset_factory(Reativacao, IdIccid, form=IdIccidForm, extra=1)
