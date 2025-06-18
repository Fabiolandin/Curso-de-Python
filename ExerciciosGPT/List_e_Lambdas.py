import math
"""
1)Crie uma lista com o quadrado apenas dos números pares de 1 a 20 usando list comprehension.
Perguntar como fazer para o numero q n passar no filtro continuar normal. - fiz sozinho +1 ponto
"""
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
quadradro = [numero * numero for numero in lista1 if numero % 2 == 0]

print(quadradro)

"""
2)Dada uma lista de nomes misturados com letras minúsculas e maiúsculas, filtre os nomes com mais de 5 letras 
e retorne todos em caixa alta. -Fiz sozinho +1 ponto
"""
nomes = ['Ana', 'CARLOS', 'joao', 'MARCELA', 'Paulo', 'fernanda']
filtro = [nome.title() for nome in nomes if len(nome) > 5]
print(filtro)

"""
3)Dado um dicionário de produtos com nome e preço, retorne apenas os nomes dos produtos com preço 
maior que R$500 usando map e filter. -N fiz, pedir pro chat explicar como fazer
"""
produtos = [
    {'nome': 'Notebook', 'preco': 2500},
    {'nome': 'Fone', 'preco': 200},
    {'nome': 'Celular', 'preco': 1800},
    {'nome': 'Carregador', 'preco': 80}
]

# Filtra produtos com preço > 500 e mapeia para seus nomes
nomes_produtos_caros = map(
    lambda produto: produto['nome'],
    filter(
        lambda produto: produto['preco'] > 500,
        produtos
    )
)

# Converte o resultado em uma lista (opcional, para visualização)
print(list(nomes_produtos_caros))

"""
4)Crie uma list comprehension que percorre uma string e substitui cada vogal por um "*". - fiz solo +1 ponto
"""
texto = "programacao"
formatacao = ['*' if vogal in 'aeiou' else vogal for vogal in texto]
print(formatacao)

"""
5)Dada uma lista de números, multiplique por 3 os ímpares e por 2 os pares, usando list comprehension. 
-fiz sozinho +1 ponto
"""
numeros = [1, 2, 3, 4, 5]
multiplicador = [numero * 3 if numero % 2 != 0 else numero * 2 for numero in numeros]

print(multiplicador)

"""
6)Crie uma lista de tuplas do tipo: (número, 'par') ou (número, 'ímpar'). - n consegui fazer solo
"""
numeros = [1, 2, 3, 4]

tuplas = [(numero, 'par' if numero % 2 == 0 else 'ímpar') for numero in numeros]
print(tuplas)

"""
7)Crie uma lista com 5 funções lambda diferentes que realizem operações com um número 
(ex: somar 2, multiplicar por 3, etc). Depois, use um for para aplicar cada função no número 10.
"""
funcoes = [
    lambda x: x + 2,
    lambda x: x * 3,
    lambda x: x - 4,
    lambda x: x / 2,
    lambda x: x ** 2
]

for funcao in funcoes:
    print(funcao(10))


"""
8)Dada uma lista de palavras, filtre aquelas que começam com a letra 'p' (minúscula), usando filter com lambda.
-somente com ajuda do chat
"""
palavras = ['python', 'java', 'programar', 'código', 'panda']

filtro = filter(lambda palavra: palavra.startswith('p'), palavras)

print(list(filtro))  # ['python', 'programar', 'panda']

"""
9)Use map e lambda para criar uma nova lista com as raízes quadradas dos números de 1 a 9. -fiz solo +1 ponto
"""
iteravel = [1, 2, 3, 4, 5, 6, 7, 8, 9]

function = lambda numeros: math.sqrt(numeros)

conversor = map(function, iteravel)
print(list(conversor))
"""
10)Ordene uma lista de palavras pelo número de letras usando sorted() e lambda.
"""
palavras = ['banana', 'uva', 'abacaxi', 'kiwi']

palavras2 = sorted(palavras, key=lambda palavra: len(palavra), reverse=True)
print(palavras2)


