"""
Funções com retorno

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ret = numeros.pop()

print(ret)

print(numeros)

Funções python que retornam valores devem conter o "Return"
"""
# Exemplo de função que retorna valor

def quadrado_de_7():
    return 7 * 7

ret = quadrado_de_7()
print(ret)

# Refatorando a primeira função

def diz_oi():
    return 'Oi! '

print(diz_oi())

alguem = 'Fabio'

print(diz_oi() + alguem) # se a func fosse print não dava pra fazer isso

"""
OBS: Sobre return
1 - Ela finaliza a função, ou seja, ela sai da execução da função
2 - Podemos ter em uma função diferentes returns
3 - Podemos, em uma função, retornar qualquer tipo de dado até o mesmo multiplos valores
"""

#Exemplo 2

def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3
    return 'b'

print(nova_funcao())

#Exemplo 3
def outra_funcao():
    return 1, 2, 3, 4

num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)

print(outra_funcao())

