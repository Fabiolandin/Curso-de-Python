"""
1)Faça um programa que determine e mostre os cinco primeiros multiplos de 3, considerando números maiores que 0.
"""
print("Os cinco primeiros múltiplos de 3 são:")
for i in range(1, 6):  # De 1 a 5 (pois 3*1, 3*2, ..., 3*5)
    print(3 * i, end=' ')

"""
2)Faça um programa que utilize o comando while, para mostrar na tela uma contagem regressiva, iniciando em 10 e
terminando em 0. Mostre também uma mensagem de "FIM" após a contagem.
"""
numero = 10

#exemplo1
while numero > 0:
    print(numero)
    numero = numero - 1
print('Fim!')
"""
3)Faça um programa que declare um inteiro, inicialize-o com 0, e incremente-o de 1000 em 1000, imprimindo seu valor
na tela, até que seu valor seja 100000.
"""
num1 = 0

#Forma 4
for num1 in range(num1, 101000, 1000):
    print(num1)
