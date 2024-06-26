import datetime
from decimal import Decimal
from .models import *


def ajustar_preco(tipo_quarto, data):
    # Fatores de ajuste baseados no dia da semana
    fator_ajuste_semana = {
        0: 1.0,  # Segunda-feira
        1: 1.0,  # Terça-feira
        2: 1.0,  # Quarta-feira
        3: 1.0,  # Quinta-feira
        4: 1.0,  # Sexta-feira
        5: 1.2,  # Sábado
        6: 1.2   # Domingo
    }

    dia_da_semana = data.weekday()
    fator_ajuste_dia = fator_ajuste_semana[dia_da_semana]

    # Calcular a ocupação atual
    ocupacao_atual = (tipo_quarto.quantidade - tipo_quarto.quartos_disponiveis) / tipo_quarto.quantidade

    if ocupacao_atual >= 0.5:
        fator_ajuste_ocupacao = 1 + ocupacao_atual
    else:
        fator_ajuste_ocupacao = 1.0

    fator_ajuste_total = fator_ajuste_dia * fator_ajuste_ocupacao
    preco_ajustado = tipo_quarto.preco_base * Decimal(fator_ajuste_total)

    # Salvar o ajuste de preço no banco de dados
    ajuste_preco, created = ajuste_preco.objects.update_or_create(
        tipo_quarto=tipo_quarto,
        data=data,
        defaults={
            'fator_ajuste': fator_ajuste_total,
            'preco_ajustado': preco_ajustado
        }
    )
    return ajuste_preco

def calcular_precos_para_mes(hotel):
    hoje = datetime.date.today()
    precos = []

    quartos = hotel.tipoquarto_set.all()

    for i in range(30):  # Calcular preços para os próximos 30 dias
        data = hoje + datetime.timedelta(days=i)
        for quarto in quartos:
            ajuste_preco = quarto.ajustar_preco(data)
            precos.append({
                'date': data.isoformat(),
                'price': float(ajuste_preco.preco_ajustado),  # Converte o preço ajustado para float para ser usado no JavaScript
                'room': quarto.tipo_quarto
            })

    return precos

def prever_precos_proximo_mes(hotel):
    return calcular_precos_para_mes(hotel)
