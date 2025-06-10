"""
Preversando metadatas com wraps

Metadatas -> São dados intrísecos em arquivos.

wraps -> São funções que envolvem elementos com diversas finalidades.
"""
# Problema -  resolvido

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função dentro de outra"""
        print(f'Voce esta chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """ Soma dois números."""
    return a + b

#print(soma(1, 2))

print(soma.__name__)
print(soma.__doc__)