"""
Levantando os próprios erros com raise

raise -> Lança exeções

OBS: não é uma função, é uma palavra reservada assim como def, ou qualquer outra em python.
para simplificar, pens eno raise como sendo util para criar nossa proprias mensagens de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')

#Exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('O texto deve ser string')
    if type(cor) is not str:
        raise TypeError('A cor deve ser string')
    print(f'O Texto {texto} sera impresso na cor {cor}')


colore('texto', 'red')

O RAISE FINALIZA A FUNÇÃO, NADA APÓS O RAISE É EXECUTADO!
"""

#Exemplo real

def colore(texto, cor):
    cores = ('Verde', 'Vermelho', 'Amarelo')
    if cor not in cores:
        raise ValueError(f'Essa cor não esta nessa lista possivel {cores}')
    if type(texto) is not str:
        raise TypeError('O texto deve ser string')
    if type(cor) is not str:
        raise TypeError('A cor deve ser string')
    print(f'O Texto {texto} sera impresso na cor {cor}')


colore('texto', 'red')