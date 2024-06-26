from .models import TipoQuarto, AjustePreco
from datetime import date, datetime

def mostrar_tipos_de_quartos():
    print('Tipos de quartos:', TipoQuarto.objects.all())

def calcular_preco():
    tipos = TipoQuarto.objects.all()
    hoje = date.today()
    
    for tipo in tipos:
        quartos_existentes = tipo.quantidade
        quartos_disponiveis = tipo.quartos_disponiveis
        ocupacao = (quartos_existentes - quartos_disponiveis) / quartos_existentes
        
        # Calcula o valor de ajuste baseado na ocupação
        if ocupacao >= 0.8:
            valor_ajuste = 1.5  # 50% de aumento se 80% ou mais ocupados
        elif ocupacao >= 0.5:
            valor_ajuste = 1.2  # 20% de aumento se 50% ou mais ocupados
        else:
            valor_ajuste = 1.0  # Sem aumento se menos de 50% ocupados
        
        # Aumenta o valor ajuste em 10% se for fim de semana (sábado ou domingo)
        if hoje.weekday() == 5 or hoje.weekday() == 6:  # 5 é sábado, 6 é domingo
            valor_ajuste *= 1.1
        
        preco_ajustado = float(tipo.preco_base) * valor_ajuste
        AjustePreco.objects.create(
            tipo_quarto=tipo, 
            data=hoje, 
            fator_ajuste=valor_ajuste, 
            preco_ajustado=preco_ajustado
        )

calcular_preco()