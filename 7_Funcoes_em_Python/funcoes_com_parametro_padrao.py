"""
Funções com parametro padrão (Default Paramters)

-Funções onde a passagem de parametros seja opcional.


"""


#Exemplo 1 - se colocarmos o valor na função, ele fica como padrão, mas pode ser alterado se repassarmos ele

def exponencial(numero=2, potencia=2):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial())

#Exemplo mais complexo
def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Fabio'
    elif nome == 'Geek':
        return 'Eu pensei que voce era o instrutor Fabio'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Gabriel', instrutor=True))

# Podemos ter funções que são declaradas dentro de funções

def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()