"""
Listas

Listas em python, funcionam como vetores/matrizes, com a diferença de serem dinamicos e também podemos colocar
qualquer tipo de dados.

As listas em Python são representadas por colchetes: []
"""

lista = [1, 2, 88, 4, 6, 2, 77, 8, 9, 10, 2]

lista2 = []

lista3 = ['F', 'A', 'B', 'I', 'O']

#Podemos facilmente checar se determinado valor está contido na lista

num = 8
if num in lista:
    print(f'Encontrei o {num}')
else:
    print(f'Não encontrei o {num}')

#Podemos facilmente ordenar uma lista
lista.sort()
print(lista)

#Imprimir uma lista inverso
lista.reverse()

#Podemos contar o número de ocorrencias de cada lista
print(lista.count(2))
print(lista3.count('O'))

#Adicionando elementos na lista
lista.append(3)
print(lista)

lista.extend([1, 2, 3])
print(lista)

#remover o ultimo elemento da lista, ou remover pelo indice
print(lista3)
lista3.pop()
print(lista3)
lista3.pop(2)
print(lista3)

"""
#Convertendo String para lista
 curso = 'Programação em Python'
 print(curso)
 curso = curso.split()
 print(curso)
"""