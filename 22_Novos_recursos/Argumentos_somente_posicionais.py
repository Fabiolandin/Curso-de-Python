"""
Argumentos Somente Posicionais

#Antes da barra os argumentos são posicionais depois somente com argumentos de parametro
def cumprimenta_v2(nome, /, altura):
    return f'Olá, {nome} e tenho {altura}'

print(cumprimenta_v2('Fabio', altura=1.75))

#Com o * todos os argumentos tem que ser informados

"""

valor = "67.3"
print(float(valor))

def cumprimenta_v1(nome):
    return f'Olá, {nome}'

print(cumprimenta_v1('Fabio'))
print(cumprimenta_v1(nome='Fabio'))

#Antes da barra os argumentos são posicionais
def cumprimenta_v2(nome, /):
    return f'Olá, {nome}'

print(cumprimenta_v2('Fabio'))
# print(cumprimenta_v2(nome='Fabio')) TypeError

#Com o * todos os argumentos tem que ser informados
def cumprimenta_v5(*, nome):
    return f'Olá, {nome}'

print(cumprimenta_v5(nome='Fabio'))