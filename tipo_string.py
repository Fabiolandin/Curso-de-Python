"""
Tipo String

Em python, um dado é considerado string sempre que:
Estiver entre aspas simples ' '
Estiver entre aspas duplas " "
Estiver entre aspas simples triplas '''  '''
"""
nome = 'Geek University'
print(nome)
print(type(nome))

print(nome.upper()) #deixa td maiusculo
print(nome.lower()) #deixa td minusculo
print(nome.split())

print(nome[0:4]) #slice de string

print(nome[::-1]) #invertendo string