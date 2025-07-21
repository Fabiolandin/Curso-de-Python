"""
Dictionary comprehension

# Sintax
{chave: valor for valor in iteravel}
"""

# Exemplos
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave : valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

# Transformando lista em dictionary
lista1 = [1, 2, 3, 4, 5]
quadrados = {valor: valor ** 2 for valor in lista1}

print(quadrados)

# Mistura
chaves = ['a', 'b', 'c', 'd']
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]:valores[i] for i in range(len(chaves))}
print(mistura)