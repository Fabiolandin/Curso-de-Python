"""
Dobro dos Números
Dada a lista [1, 2, 3, 4, 5], crie uma nova lista com o dobro de cada número usando list comprehension.
"""
numeros = [1, 2, 3, 4, 5]

print([numero * 2 for numero in numeros])

"""
Números Pares
Dada a lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crie uma lista apenas com os números pares usando list comprehension.
"""
numeros2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [numero for numero in numeros2 if not numero % 2]
print(pares)

"""
Primeira Letra Maiúscula
Dada a lista de nomes ['maria', 'joão', 'pedro', 'ana'], crie uma nova lista com os nomes capitalizados (primeira letra maiúscula).
"""
nomes = ['mAria', 'jOão', 'pedro', 'ana']
nomesformatados = [nome.split()[0].title() for nome in nomes]
print(nomesformatados)

"""
Quadrados dos Ímpares
Dada a lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crie uma lista com os quadrados apenas dos números ímpares.
"""
lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = [numero * numero for numero in lista3 if numero % 2]
print(impares)

"""
Filtrando Strings Curtas
Dada a lista ['python', 'java', 'c', 'javascript', 'go', 'ruby'], crie uma lista apenas com as palavras que têm mais de 3 letras.
"""
linguagens = ['python', 'java', 'c', 'javascript', 'go', 'ruby']
#Crie uma lista com cada palavra,
# para cada palavra dentro da lista linguagens
# se a palavra tiver mais de 3 letras retorne ela.
filtro = [palavra for palavra in linguagens if len(palavra) > 3]
print(filtro)