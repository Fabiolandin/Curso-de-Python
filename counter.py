"""
Módulo Collections - Counter
Collections -> High-performance Container Datetypes

Counter -> Recebe um interável como parametro e cria um objeto do tipo Collections Counter que é parecido
com dicionario.
"""

#Utilizando o Counter

from collections import Counter

# Exemplo2
#Podemos utilizar qualquer iteravel aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 4, 4, 5]

#Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)

"""
Ele retornou : Counter({5: 4, 1: 3, 2: 3, 3: 3, 4: 3})
Ele soma a quantidade de cada numero em especifico
"""

print(Counter('Fabio Tamburi Landin Junior'))