"""
List comprehension - parte 2

Nós podemos adicionar estruturas condicionais lógicas as nossas list comprehension

"""

# Exemplo
#1

numeros = [1, 2, 3, 4, 5]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

#Refatorando - List Comprehension
pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)