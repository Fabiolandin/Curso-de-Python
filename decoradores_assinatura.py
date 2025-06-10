"""
Decorators com diferentes assinaturas

# Para resolver, utilizamos um padrão de projeto chamado Decorator Pattern

A assinatura de uma função e representada pelo seu retorno, nome e parametros de entrada.
"""

#Com decorator patttern

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal} acompanhado de {acompanhamento}'

print(saudacao('Fabio'))

print(ordenar('Picanha', 'Batata Frita'))

#Obs: vale lembrar que podemos utilizar parametros nomeados

print(ordenar(acompanhamento='Batata Frita', principal='Picanha'))

#Decorator com argumentos
def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser o {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica_primeiro_argumento('Pizza')
def comida_favorita(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

#Testando
print(soma_dez(10, 12)) #22
print(soma_dez(1, 21))

print(comida_favorita('Pizza', 'Churrasco'))
print(comida_favorita('Hamburguer', 'Pizza'))