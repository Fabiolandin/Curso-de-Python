"""
Listas aninhadas (nested lists)

"""

#Exemplos
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #Matriz 3x3

# Como fazemos para acessar os dados
print(listas[0][1]) #2
print(listas[2][1])

# Iterando com loops em uma lista aninhada
for lista in listas:
    for numero in lista:
        print(numero)

print('\n \n')

# List Comprehension
[[print(valor) for valor in lista] for lista in listas]


#Outros Exemplos

#Gerando uma matriz 3x3

tabuleiro = [[numero for numero in range(1,4)] for valor in range(1,4)]
print(tabuleiro)