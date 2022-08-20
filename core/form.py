from django import forms
from .models import Eventos

class FormEventos(forms.ModelForm):
    class Meta:
        model = Eventos
        exclude = ()

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control','autofocus': ''}),
            'descricao': forms.TextInput(attrs={'class': 'form-control','autofocus': ''}),
            'data_evento':forms.DateInput(attrs={'class':'form-control'}),
            'salario' :forms.NumberInput(attrs={'class':'form-control'}),
            'data_criacao' :forms.DateInput(attrs={'class':'form-control'}),
            'usuario' :forms.Select(attrs={'class': 'form-select','autofocus': ''})

       }