"""
Debugando com PDB

PDB -> Python Debugger

A utilização de print para debbug é uma pratica ruim!

Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger

#Exemplo com Python Debugger
#Para utilizar o PDB precisamos importar a biblioteca e então utilizar a função set_trace()

#comandos básicos do PDB
# l lista aonde estamos no código
# n próxima linha
# p imprime variavel
# c continua a execução - finaliza o debugging
import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' ' + curso
print(final)

A PARTIR DA VERSÃO 3.7 DO PYTHON O PDB VIROU UMA FUNC BUILT-IN, breakpoint()

"""
nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' ' + curso
print(final)
