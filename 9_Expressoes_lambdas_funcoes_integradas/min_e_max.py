"""
Min e Max

Funciona pra tupla, conjunto, dicionario, lista.

max() -> retorna o maior valor
min() -> retorna o menor valor
"""
#exemplos
lista = [1, 22, 399, 4, 5, 61]
print(max(lista))
print(min(lista))

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 129}
print(max(dicionario.values()))

#Faça um programa que receba dois valores e informe o maior
val1 = int(input('Digite um valor: '))
val2 = int(input('Digite outro valor: '))

print(max(val1, val2))

#Outros exemplos
nomes = ['Marcos', 'Marcela', 'Ana Maria', 'Sarah Oliveira', 'Bruno Sergio']

print(max(nomes))
print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

