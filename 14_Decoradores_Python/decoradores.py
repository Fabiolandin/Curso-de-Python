"""
Decoradores (Decorators)

O que são decorators?
- Decorators são funções.
- Decorators envolvem outras funções e aprimoram os seus comportamentos.
- Decorators também são exemplos de Higher Order Functions.
- Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar / Açucar Sintatico)
"""
#Decorators como funções (Sintaxe não recomendada / Sem açucar sintatico)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer te conhecer!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo

def saudacao():
    print('Seja bem vindo a Geek University!')

#Testando

#Saudacao()
teste = seja_educado(saudacao)

teste()

#Testando 2

def raiva():
    print('EU TE ODEIO!')

raiva_educada = seja_educado(raiva)

#raiva_educada()

print('\n')

#Decorators com Syntax Sugar (Açucar Sintatico) RECOMENDADO
def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer te conhecer!')
        funcao()
        print('Tenha um Ótimo dia!')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Fabio')

#Testando
apresentando()


