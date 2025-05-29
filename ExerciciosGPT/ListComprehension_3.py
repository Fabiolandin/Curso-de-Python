"""
filter() com lambda
Objetivo: filtrar valores com base em uma condição (True/False)
"""
numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4]

"""
map() com lambda
Objetivo: aplicar uma função a todos os itens de uma lista
"""
numeros = [1, 2, 3]
dobro = list(map(lambda x: x * 2, numeros))
print(dobro)  # [2, 4, 6]

"""
sorted() com lambda
Objetivo: ordenar itens com base em alguma "chave" (por ex: tamanho de string)
"""
palavras = ['uva', 'abacaxi', 'kiwi', 'banana']
ordenadas = sorted(palavras, key=lambda p: len(p))
print(ordenadas)  # ['uva', 'kiwi', 'banana', 'abacaxi']

"""
Lista de funções lambda
Objetivo: criar uma lista de funções diferentes e aplicar uma a uma
"""
funcoes = [
    lambda x: x + 2,
    lambda x: x * 3,
    lambda x: x - 1,
    lambda x: x ** 2,
    lambda x: x % 2
]

for f in funcoes:
    print(f(10))
# Saída: 12, 30, 9, 100, 0

"""
Exercicios
1)Use filter() com lambda para filtrar números maiores que 5 de uma lista.
"""
numeros = [1, 2, 3, 4, 5]
filtro = list(filter(lambda x: x > 5, numeros))
print(filtro)

"""
2)Use map() com lambda para transformar uma lista de strings em maiúsculas.
"""
palavras = ['the last of us', 'god of war', 'minecraft']
maiuscula = list(map(lambda palavra: palavra.upper(), palavras))
print(list(maiuscula))

"""
3)Use sorted() com lambda para ordenar uma lista de dicionários por valor numérico:
"""
itens = [{'nome': 'a', 'preco': 10}, {'nome': 'b', 'preco': 5}]
ordenacao = sorted(itens, key=lambda item: item['preco'])
print(ordenacao)

"""
4)Crie uma lista com 3 lambdas que: somam 5, multiplicam por 2 e elevam ao quadrado. Aplique elas no número 4.
"""
listalambda = [
    lambda x: x + 5,
    lambda x: x * 2,
    lambda x: x ** 2
]

for f in listalambda:
    print(f(4))