from django.db import models
from django.contrib.auth.models import User
from .predicao import ajustar_preco

class Hotel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = 'Hoteis'

class TipoQuarto(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    tipo_quarto = models.CharField(max_length=50)
    preco_base = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    quartos_disponiveis = models.IntegerField()

    def __str__(self):
        return f'{self.hotel.nome} - {self.tipo_quarto}'
    
    class Meta:
        verbose_name_plural = 'Tipos de quartos'

    def ajustar_preco(self, data):
        return ajustar_preco(self, data)

class AjustePreco(models.Model):
    tipo_quarto = models.ForeignKey(TipoQuarto, on_delete=models.CASCADE)
    data = models.DateField()
    fator_ajuste = models.FloatField()
    preco_ajustado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.tipo_quarto} - {self.data}'
    
    class Meta:
        verbose_name_plural = 'Ajustes de precos'
