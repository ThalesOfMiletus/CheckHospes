# precificacao/forms.py

from django import forms
from .models import *

class TipoQuartoForm(forms.ModelForm):
    class Meta:
        model = TipoQuarto
        fields = ['tipo_quarto', 'preco_base', 'quantidade', 'quartos_disponiveis']

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['nome', 'localizacao']