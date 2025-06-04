"""
Sistema de arquivos - Manipulação

"""
import os

#Descobrindo se um arquivo existe
print(os.path.exists('frutas.txt')) #True

#Descobrindo se um diretório existe - relativos
print(os.path.exists('Pandas')) # True
print(os.path.exists('geek/university')) # True

#Paths absolutos
print(os.path.exists('geek/university/geek3.py')) # True

#Criando arquivos
#Forma 1
open('arquivo-teste.txt', 'w').close()

#Forma 2
open('arquivo-teste2.txt', 'a').close()

#Forma Correta
os.mknod('arquivo4.txt')

#Criando diretórios - Path relativo
os.mkdir('templates')

#Criando multiplos diretórios de uma vez
os.makedirs('templates/geek/university')

#Renomear arquivos e diretórios
os.rename('Exercicios_curso', 'Exercicios_do_curso')
os.rename('geek/university/geek3', 'geek/university/geek')

#Deletando arquivos - tome cuidado, ao deletarmos o arquvi/diretório eles não iram para a lixeira!!!
os.remove('arquivo.txt')

#Deletando diretórios - vazios - se tiver qualquer conteudo nao deleta
os.rmdir('templates')
