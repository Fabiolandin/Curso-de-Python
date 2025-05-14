"""
Entendendo args

Args é um parametro como outro qualquer, isso significa que voce podera chamar qualquer outra coisa, desde que comece
com o asterisco

Args é um parametro utilizado em func, coloca os valores extras informados como entrada em uma tupla.(imutaveis)
"""
# Entendendo Args
def soma_numeros(*args):
    return sum(args)

print(soma_numeros(1, 2, 3))

# Outro exemplo da utilização do *args
def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vindo!'
    return 'Eu não sei quem voce é...'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.154))

# Ex 3
def soma_numeros(*args):
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Desempacotando
print(soma_numeros(*numeros))
