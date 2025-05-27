"""
Aplicando Desconto
Dada uma lista de preços [50, 100, 150, 200], use map() para aplicar um desconto de 10%
Implemente com lambda e depois com função normal
"""
lista = [50, 100, 150, 200]
desconto10 = lambda preco: -(preco * 10 / 100) + preco

print(list(map(desconto10, lista)))


def desconto(x):
    return -(x * 10 / 100) + x

desconto10 = map(desconto, [50, 100, 150, 200])
print(list(desconto10))

"""
Formatando Nomes
Dada a lista de nomes ['maria', 'joão', 'PEDRO'], use map() para:
a) Colocar todos em maiúsculo
b) Capitalizar (primeira letra maiúscula)
"""
lista2 = ['maRia', 'joão', 'PEDRO']
nomesformatados = lambda nomes: nomes.strip().title()

print(list(map(nomesformatados, lista2)))

"""
Calculando Áreas
Dada uma lista de raios [1, 2, 3, 4, 5], calcule:
a) A circunferência (2 * π * r)
b) A área do círculo (π * r²)
Use map() e math.pi
"""
import math
lista = [1, 2, 3, 4, 5]

calculoa = lambda raios: 2 * math.pi * raios
calculob = lambda raios: math.pi * raios * raios

print(list(map(calculoa, lista)))
print(list(map(calculob, lista)))



