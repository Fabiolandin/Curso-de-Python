from math import sqrt
"""
1)Faça um programa que receba dois números inteiros e mostre qual deles é maior.
"""
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))
if num1 > num2:
    print('O número 1 é maior que o número 2')
elif num1 == num2:
    print('Os números são iguais')
else:
    print('O número 2 é maior que o número 1')


"""
2)Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule a raiz
quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o número é invalido.
"""
if num1 > 0:
    num3 = sqrt(num1)
    print(num3)
else:
    print('Esse número não é valido')


"""
3)Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.
"""
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")