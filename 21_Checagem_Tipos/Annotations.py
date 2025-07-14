"""
Correto
texto: str

Incorreto
texto:str

Correto
) -> str:

Incorreto
) ->str:
"""

import math

def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio

print(circunferencia.__annotations__)

nome: str = 'Geek University'

peso: float = 82.9

ativo: bool = True

print(nome, peso, ativo)
print(__annotations__)

class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso

    def andar(self) -> str:
        return 'Esta andando!'

p = Pessoa(nome='Geek University', idade=18, peso=82.9)

#print(p.__annotations__) nÃO TEM ANNOTATIONS

print(p.andar.__annotations__)