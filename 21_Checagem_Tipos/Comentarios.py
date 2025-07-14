"""
da pra chamar o mypy dessa forma também.
"""
import math

def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio

print(circunferencia(8))

def cabecalho(texto, alinhamento = True):
    #type: (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'