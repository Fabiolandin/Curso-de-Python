"""
Pacotes

Módulo -> é apenas um arquivo em python que pode ter diversas funções para utilizarmos
Pacote -> É um diretório contendo uma coleção de módulos

"""
import geek.geek2
from geek import geek1, geek2
from geek.university import geek3, geek4

print(geek1.pi)

print(geek1.funcao1(4, 6))

print(geek2.curso)

print(geek.geek2.funcao2())

print(geek3.funcao3())

print(geek4.funcao4())

#importando somnte a func 1 dentro do módulo 1
from geek.geek1 import funcao1
print(funcao1(4, 6))