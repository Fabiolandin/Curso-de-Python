"""
Reduce

A partir do python 3 a função reduce não é mais uma função integrada, agora precisa importar 'functools'

Para entender o reduce()
"""
from functools import reduce

#Exemplo 01
dados = [2, 3, 4, 5, 11, 24, 25, 29]

#Para utilizar o reduce precisamos de uma função que receba dois parametros
multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

#Como geralmente é feito (QUEM N MANJA DE PYTHON)
res = 1
for n in dados:
    res = res * n

print(res)
