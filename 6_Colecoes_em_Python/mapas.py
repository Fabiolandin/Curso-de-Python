"""
Mapas -> Conhecidos em Python como Dicionarios

Dicionarios em python são representados por chaves {}
"""

receita = {'jan': 100, 'fev':120, 'mar': 300}

#iterar dentro de dicts
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita.keys():
    print(receita[chave])

#Acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)


#Desempacotamento de dicionarios
for chave, valor in receita.items():
    print(f'Chave = {chave} Valor = {valor}')