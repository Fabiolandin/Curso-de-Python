"""
1. Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores
lidos.
"""
lista1 = []
print(type(lista1))
for contador in range(1, 7):
    num1 = input("Digite um número inteiro: ")
    lista1.append(num1)

print(lista1)


"""
2. Faça um programa que possua uma lista denominada A que armazene 6 números inteiros. O programa
deve executar os seguintes passos:
a) Atribua os seguintes valores a essa lista: 1, 0, 5, -2, -5, 7.
b) Armazene em uma variável inteira a soma entre os valores das posições A[0], A[1] e A[5] da lista e mostre
na tela esta soma.
c) Modifique a lista na posição 5, atribuindo a esta posição o valor 100.
d) Mostre na tela cada valor da lista A, um em cada linha.
"""
listaA = [1, 0, 5, -2, -5, 7.]
print(listaA)

soma = listaA[0]+listaA[1]+listaA[5]
print(f'A soma da lista do exercicio 2 é {soma}')

listaA[5] = 100

for numero in listaA:
    print(numero)


"""
3. Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele
possui.
"""
numeros = []
pares = 0

for _ in range(10):
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)

    if num % 2 == 0:
        pares += 1

print(f"A lista contém {pares} números pares.")
print(f"Lista completa: {numeros}")