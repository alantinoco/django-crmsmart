from django import forms
from .models import Contato, Venda

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = '__all__'