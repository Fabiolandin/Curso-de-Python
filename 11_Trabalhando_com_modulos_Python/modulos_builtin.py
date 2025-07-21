"""
Trabalhando com módulos Builtin (módulos integrados, que já vem instalados no Python)

#Podemos importar todas as funções de um módulo utilizando o *
from random import *
#Impor random
"""
#Utilizando alias (apelidos) para módulos/funções
import random as rdm

print(rdm.random())

#ex 2
from random import randint as rdi, random as rdma

print(rdi(5, 89))
print(rdma())