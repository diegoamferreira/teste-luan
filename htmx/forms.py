from django import forms

from fusion.models import Service


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ['titulo', 'descricao', 'icone', 'empresa']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'autofocus': ''}),
            'icone': forms.Select(attrs={'class': 'form-control'}),
            'empresa': forms.Select(attrs={'class': 'form-control'}),

        }
