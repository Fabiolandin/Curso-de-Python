"""
Módulo Collections - Named Tuple

Named Tuple -> São tuplas diferenciadas onde especificamos um nome para a mesma e parametros.
"""
#importanto

from collections import namedtuple

#Precisamos definir o nome e parametros

# Forma 1
cachorro = namedtuple('cachorro','idade raca nome')

# Forma 2
cachorro = namedtuple('cachorro','idade, raca, nome')

# Forma 3
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando
ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

print(ray)

print(ray[0])
print(ray[1])
print(ray.nome)