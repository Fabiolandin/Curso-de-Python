"""
Funções com parametro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma

Se a gente pensar em um programa qualquer, geralmente temos:
entrada > processamento > saida


"""
# Refatorando uma função
def quadrado_de_num(num):
    ##return num * num
    return num ** 2

print(quadrado_de_num(4))

#Refatorando outra função
def cantar_parabens(aniversariante):
    print('Parabens pra voce')
    print('Nesta data querida!')
    print('Muitas felicidades!')
    print('Muitos anos de vida!')
    print(f'Viva o {aniversariante}!')

cantar_parabens('Fabio')

def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outa(num1, b, msg):
    return (num1 + b) * msg

print(soma(4, 5))
print(multiplica(4, 5))
print(outa(3, 2, 'Geek'))

#Nomeando parametros
def nome_completo(nome, sobrenome):
    return f' Seu nome completo é {nome} {sobrenome}'

print(nome_completo(nome='Fabio', sobrenome='Landin'))