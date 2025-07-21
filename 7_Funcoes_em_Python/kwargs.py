"""
**kwargs

Este é so mais um parametro porém diferente do args ele coloca os valores extras em um dicionario.

os parametros args e kwargs não são obrigatórios.
"""

#Exemplo
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'O {pessoa.title() } prefere a cor {cor}')

cores_favoritas(marcos='verde', fabio='azul', leo='preto')

#Exemplo mais complexo
def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Voce recebeu um cumprimento do Python!'
    elif 'geek' in kwargs:
        return f'{kwargs["geek"]} Geek!'
    return 'Não tenho certeza de quem você é...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='Especial'))

# Desempacotar **kwargs

def mostra_nomes(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}'

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}
print(mostra_nomes(**nomes))

