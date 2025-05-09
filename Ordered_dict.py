"""
Módulo Collections: Ordered Dict

"""
# Em um dicionario, a ordem de inserção não é garantida.
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# Fazendo import
from collections import OrderedDict

dicionario1 = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})

for chave, valor in dicionario1.items():
    print(f'Chave = {chave}, Valor = {valor}')
