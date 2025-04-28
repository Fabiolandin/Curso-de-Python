"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas
"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que trasnformar em lista

# Exemplo de for 1
for letra in nome:
    print(letra)

# Exemplo de for 2
for numero in lista:
    print(numero)

# Exemplo de for 3
for numero in range(1, 10):
    print(numero)


qtd = int(input('Quantas vezes esse loop deve rodar?'))

for n in range(1, qtd + 1):
    print(f'Imprimindo {n} vez')

"""
qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f'Informe p {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma dos valores {soma}')
"""