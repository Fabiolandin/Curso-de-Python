"""
Aula 2 sobre listas em Python

Só reforçando que a lista pode incluir varios tipos de dados
lista6 = [1, 2, 3, True, 'Fabio', [1, 2, 3]]
print(lista6)
print(type(lista6))
"""

lista1 = [1, 2, 3, 5, 6, 9, 10]

lista2 = ['F', 'A', 'B', 'I', 'O']

#Utilizando for
for elemento in lista1:
    print(elemento)

#Utilizando While
"""
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digitie 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
"""

cores = ['verde', 'amarelo', 'verde', 'azul']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

#Encontrar o indice de um elemento da lista
print(lista1.index(6))

print(sum(lista1)) #soma
print(max(lista1)) #valor maior
print(min(lista1)) #valor menor
print(len(lista1)) #tamanho da lista

