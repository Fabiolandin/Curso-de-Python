"""
Funções de Maior Grandeza - Higher Order Functions - HOF

O que isso significa?

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções
como resultado ou mesmo que podemos passar funções como argumentos para outras funções, e até mesmo criar variaveis do
tipo de funções nos nossos programas.

OBS: Na sessão de funções utilizamos isso.

EM python, as funções são cidadões de Primeira Classe, First Class Citizen
"""
# Exemplo - Definindo as funções

def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

#Testando as funções
print(calcular(1, 2, somar))
print(calcular(1, 2, diminuir))
print(calcular(1, 2, multiplicar))
print(calcular(1, 2, dividir))

#Nested Functions - Funções Aninhadas

"""
Em python podemos também ter funções dentro de funções, que são conhecidas por Nested Functions
ou também Inner functions (funções internas)
"""

#Exemplo

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa

print(cumprimento('Flavia'))
print(cumprimento('Bianca'))

# Retornando funções de outras funções

def faz_me_rir():
    def rir():
        return choice(('HAHAHAHAHA', 'N teve graça mano', 'HAUEHUEHUEHUHUEHEUEU'))
    return rir()

rindo = faz_me_rir()
print(rindo)

#Inner functions - Funções internas - Podem acessar o escopo de funções externas
def faz_me_rir_novamente(pessoa):
    def dando_risada():
        r = choice(('HAHAHAHAHA', 'N teve graça mano', 'HAUEHUEHUEHUHUEHEUEU'))
        return f'{r} {pessoa}'
    return dando_risada()

rindo = faz_me_rir_novamente('Fabio')
print(rindo)
print(rindo)