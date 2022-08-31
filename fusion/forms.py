from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        #fields = ['nome","data", 'habilitado']   #uma opção
        #fields = '__all__'
        exclude = ["empresa"]

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nome','data-error':"Por favor digite seu nome", 'required':'requirid'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email','data-error':"Por favor digite seu email", 'required':'requirid'}),
            'assunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Assunto','data-error':"Por favor digite um assunto", 'required':'requirid'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Sua mensagem','data-error':"Por favor digite uma mensagem", 'required':'requirid'}),


        }