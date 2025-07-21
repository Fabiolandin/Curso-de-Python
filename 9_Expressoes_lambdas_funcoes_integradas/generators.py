"""
Generators

Tuple comprehension se chamam generators
"""
import sys

nomes = ['Carlos', 'Camila', 'Cassiano', 'Cristina']

#List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

#Generator - mais leve, mais performatico
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

#Getsizeof retorna a quantidade de bytes do elemento passado pelo parametro
print(sys.getsizeof('Geek'))
