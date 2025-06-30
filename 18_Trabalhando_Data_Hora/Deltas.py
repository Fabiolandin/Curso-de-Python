"""
Trabalhando com deltas de data e hora

delta = data_final - data_inicial
"""
import datetime

#data de hoje
data_hoje = datetime.datetime.now()

#data para ocorre um determinado evento no futuro
aniversario = datetime.datetime(2026, 3, 3, 0)

#calculando delta
tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))
print(tempo_para_evento)
print(f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 60 // 60} horas')

#exemplo2
data_da_compra = datetime.datetime.now()
print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto
print(vencimento_boleto)