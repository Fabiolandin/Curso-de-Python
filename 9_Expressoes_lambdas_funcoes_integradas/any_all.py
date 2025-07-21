"""
Any e All

all() -> Retorna True se todos os elementos do iteravel são verdadeiros ou ainda se o iteravel esta vazio.

Any() -> retorna true se qualquer elemento for verdadeiro, se o iteravel estiver vazio retorna false
"""

#Exemplo All()
print(all([0, 1, 2, 3, 4])) #False
print(all([1, 2, 3, 4])) #True
print(all([])) #True

nomes = ['Carlos', 'Camila', 'Cassiano', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes]))

#Exemplos Any()
print(any([0, 1, 2, 3, 4])) #True
print(any([0, False, {}, ()])) #False

print(any([nome[0] == 'C' for nome in nomes]))





