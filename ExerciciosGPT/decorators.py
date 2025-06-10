"""
HOF + Funções como argumento
A)Crie uma função executar_operacao(a, b, operacao) que aceita qualquer função matemática (soma, divisão, potência, etc).
B)Passe funções anônimas (lambda) como operação.
"""
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def executar_operacao(num1, num2, funcao):
    return funcao(num1, num2)

#Testando as funções
print(executar_operacao(1, 2, soma))
print(executar_operacao(1, 2, divisao))

"""
Funções Aninhadas
A)Crie uma funç mensagem_personalizada(usuario) que retorna uma saudação diferente dependendo da hora do dia (simulada com random.choice).
B)A função interna deve gerar a saudação.
"""
from random import choice

def mensagem_personalizada(usuario):
    def gerar_saudacao():
        return choice(('Olá bom dia! ', 'Boa tarde! ', 'Não me peça nada que estou indo embora já '))
    return gerar_saudacao() + usuario

print(mensagem_personalizada('Flavia'))

"""
Retorno de função
Crie gerador_de_mensagem(tipo) que retorna uma função que imprime "Bom dia", "Boa tarde" ou "Boa noite".
"""
def gerador_de_mensagem(tipo):
    def funcao():
        return choice(('Bom dia', 'Boa tarde', 'Boa noite'))
    return funcao

mensagem = gerador_de_mensagem()
print(mensagem)

"""
Decoradores Simples
Crie um decorador logar_execucao que imprime:
o nome da função
os argumentos
o resultado
"""





"""
Decorador com Argumento
Crie um decorador requer_permissao("admin") que só permite executar uma função se o primeiro argumento for "admin".
"""


