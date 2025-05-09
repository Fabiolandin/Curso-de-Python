"""
Módulo Collections - Default Dict

Default dict -  ao criar um dicionario nós informamos um valor default, podendo utilizar lambda para isso.
Caso tentamos acessar uma chave que não existe, essa chave será criada e o valor default será atribuido.
"""
#import da collection
from collections import defaultdict


dicionario = {'Curso' : 'Curso de Python'}
print(dicionario)
print(dicionario['Curso'])

dicionario1 = defaultdict(lambda: 0)

dicionario1['curso'] = 'Curso de Node'
print(dicionario1)

print(dicionario1['outro'])

