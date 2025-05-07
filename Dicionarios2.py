"""
Segunda aula de dicionarios
"""

receita = {'jan': 100, 'fev':120, 'mar': 300, 'mai': 600}
print(receita)

# Atualizando dados em um dicionario

# Forma 1
receita['mai'] = 500
print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)


#Remover dados de um dicionario

#Forma 1
ret = receita.pop('mar')
print(ret)
print(receita)

#Forma 2
del receita['fev']
print(receita)

