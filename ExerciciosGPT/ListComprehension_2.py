"""
Conversão de Temperatura
Dada a lista de temperaturas em Celsius [0, 20, 30, 40, 100], crie uma lista com as temperaturas convertidas para Fahrenheit (F = C * 9/5 + 32).
"""
linguagens = ['python', 'java', 'c', 'javascript', 'go', 'ruby']
#Crie uma lista com cada palavra,
# para cada palavra dentro da lista linguagens
# se a palavra tiver mais de 3 letras retorne ela.
filtro = [palavra for palavra in linguagens if len(palavra) > 3]
print(filtro)

temperaturas = [0, 20, 30, 40, 100]
conversao =[temperatura * 9/5 + 32 for temperatura in temperaturas ]
print(conversao)

"""
Números e seus Status
Dada a lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crie uma lista de strings no formato:
"Número X é par" ou "Número X é ímpar" para cada número.
"""
paresimpares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = [f'Número {x} é {'par' if x % 2 == 0 else 'impar'}' for x in paresimpares]
print(resultado)

"""
Dada a lista
Crie uma nova lista aplicando 10% de desconto nos produtos que custam mais de R$100.
"""
produtos = [
    {'nome': 'Notebook', 'preco': 2500},
    {'nome': 'Mouse', 'preco': 50},
    {'nome': 'Teclado', 'preco': 100},
    {'nome': 'Monitor', 'preco': 800}
]

produtoscomdesconto = [{**produto, 'preco': produto['preco'] * 0.9} for produto in produtos if produto['preco'] > 100]

print(produtoscomdesconto)
"""
Múltiplas Condições
Dada a lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crie uma lista que:
Substitua números pares por "par"
Substitua números ímpares divisíveis por 3 por "ímpar3"
Mantenha os outros números como estão
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sub =["par" if numero % 2 == 0 else "impar3" if numero % 2 != 0 and numero % 3 == 0 else numero for numero in lista]
print(sub)

"""
List Comprehension + Funções
Dada a lista ['fabio', 'guilherme', 'carlos', 'marcos'], use a função caixa_alta do exemplo e list comprehension 
para criar uma lista com os nomes capitalizados.
"""
# Exemplo 3
def caixa_alta(nome):
    nome = nome.split()[0].title()
    return nome

#List Comprehension
amigos = ['fabio', 'guilherme', 'carlos', 'marcos', 'fabiano']
print([caixa_alta(amigo) for amigo in amigos])