"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer do nosso código. previnindo assim que o programa
para de funcionar e o usuario receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problematica
except:
    //o que deve ser feito em caso de problema
"""

#Exemplo 1 - tratando um erro genérico - tratar erro de forma genérica n é a melhor forma.
try:
    geek()
except:
    print('Deu algum b.o')

# Exemplo 2 - Tratando um erro especifico
try:
    geek()
except NameError:
    print('A func que voce esta usando é inexistente')

#Exemplo 3 - Tratando um erro especifico
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

try:
    len(5)
except NameError as erra:
    print(f'Deu NamedError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')