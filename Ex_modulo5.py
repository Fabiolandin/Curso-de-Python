"""
1. Crie um programa que tenha uma função que recebe um parâmetro inteiro e devolve o seu dobro.
"""
def dobra(num):
    return num * 2

print(dobra(5))


"""
2. Faça um programa que tenha uma função que recebe uma data no formato string exemplo “01/01/2024” e
imprima ela por extenso como “1 de janeiro de 2024”.
"""






"""
3. Faça um programa que tenha uma função que receba uma lista de inteiros e retorne o maior valor.
"""
def maior(lista):
    maior = 0
    for num in lista:
        if num > maior:
            maior = num
    return maior

lista = [1, 2, 3, 4, 5, 88, 7, 8, 9, 10]
print(maior(lista))