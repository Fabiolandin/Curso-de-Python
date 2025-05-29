"""
Filter com lambda
1)Filtre apenas os números pares de uma lista.
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filter(lambda num: num % 2 == 0, numeros)
print(list(pares))

"""
Filter com lambda
2)Filtre palavras que têm mais de 5 letras.
"""
palavras = ['python', 'java', 'c', 'javascript', 'go', 'ruby']
filtros = filter(lambda palavra: len(palavra) > 5, palavras)

print(list(filtros))
"""
Filter com lambda
3)Filtre dicionários com valor maior que 100.
"""
produtos = [{'nome': 'A', 'preco': 50}, {'nome': 'B', 'preco': 120}, {'nome': 'C', 'preco': 300}]
maiorvalor = filter(lambda produto: produto['preco'] > 100, produtos)

print(list(maiorvalor))

"""
map() com lambda
4)Dobre os valores de uma lista de números.
"""
numeros = [1, 2, 3, 4, 5]
dobrados = map(lambda x: x*2, numeros)

print(list(dobrados))

"""
map() com lambda
5)Transforme cada string em sua primeira letra maiúscula.
"""
nomes = ['ana', 'bruno', 'carla']
formatacao = map(lambda nome: nome.title(), nomes)
print(list(formatacao))

"""
map() com lambda
6)Adicione um campo “com desconto” aos dicionários. - necessitei de ajuda do chat
"""
produtos = [{'nome': 'A', 'preco': 100}, {'nome': 'B', 'preco': 200}]
# Resultado esperado: [{'nome': 'A', 'preco': 100, 'com_desconto': 90}, ...]

descontos = map(lambda p: {**p, 'com_desconto': p['preco'] * 0.9}, produtos)
print(list(descontos))
"""
sorted() com lambda
7)Ordene nomes por ordem alfabética inversa.
"""
nomes = ['ana', 'bruno', 'carla', 'zeca']
nomesordenados = sorted(nomes, key=lambda nome: nome, reverse=True)
print('Exercicio 7')
print(nomesordenados)
"""
sorted() com lambda
8)Ordene uma lista de tuplas pelo segundo valor.
"""
notas = [('ana', 7), ('bruno', 9), ('carla', 6)]

tuplasordenadas = sorted(notas, key=lambda notas: notas[1], reverse=True)
print(tuplasordenadas)
"""
sorted() com lambda
9)Ordene dicionários por tamanho do nome.
"""
usuarios = [{'nome': 'ana'}, {'nome': 'bruninho'}, {'nome': 'bia'}]

nomesordenados = sorted(usuarios, key=lambda p: p['nome'])
print(nomesordenados)

"""
🧠 Lista de funções lambda
10. Crie uma lista com 4 lambdas:
Soma 10
Subtrai 3
Multiplica por 4
Divide por 2
E aplique todas no número 8.
"""
calculadora = [
    lambda x: x + 2,
    lambda x: x * 3,
    lambda x: x - 4,
    lambda x: x / 2,
]

for funcao in calculadora:
    print(funcao(8))
