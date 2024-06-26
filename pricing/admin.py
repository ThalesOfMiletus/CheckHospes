# precificacao/admin.py

from django.contrib import admin
from .models import Hotel, TipoQuarto, AjustePreco

class HotelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'localizacao', 'user')

class TipoQuartoAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'tipo_quarto', 'preco_base', 'quantidade', 'quartos_disponiveis')

class AjustePrecoAdmin(admin.ModelAdmin):
    list_display = ('tipo_quarto', 'data', 'fator_ajuste', 'preco_ajustado')

admin.site.register(Hotel, HotelAdmin)
admin.site.register(TipoQuarto, TipoQuartoAdmin)
admin.site.register(AjustePreco, AjustePrecoAdmin)
