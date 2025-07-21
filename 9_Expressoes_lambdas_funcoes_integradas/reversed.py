"""
Reversed
OBS: Não confunda com a função reverse() que estudamos nas listas.

A função reverser() só funciona em listas.

Já a função reversed() funciona com qualquer iteravel.
"""

#Exemplos
lista = [1, 2, 3, 4, 5]

res = reversed(lista)
print(res)

#tem que converter
print(list(reversed(lista)))
print(set(reversed(lista))) # Em conjunto não definimos a ordem dos elementos.
print(tuple(reversed(lista)))

#Podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end='')

print('\n')

#Podemos fazer o mesmo sem o uso do for
print(''.join(reversed('Geek University')))

#ja vimos como fazer isso mais fácim com slice de strings
print('Geek University'[::-1])

#Imprimindo de trás pra frente
geek = 'Geek University'

for i in range(len(geek)-1, -1, -1):
    print(geek[i], end='')

