"""
List Comprehension

- Utilizando list comprehension nos podemos gerar novas listas com daods processados a partir de outro iteravel.

# Sintaxe da list comprehension
[ dado  for dado in iteravel ]
"""

#Exemplos
numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]
print(res)

"""
Para entender melhor oque esta acontecendo devemos dividir a expressão em duas pertes
1 - for numero in numeros
2 - numero * 10
"""

res = [numero / 2 for numero in numeros]
print(res)

#List comprehension vs Loop

#Loop
numeross = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeross:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

#List comprehension
print([numero * 2 for numero in numeros])

# Exemplo 3
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

#List Comprehension
amigos = ['fabio', 'guilherme', 'carlos', 'marcos', 'fabiano']
print([caixa_alta(amigo) for amigo in amigos])
