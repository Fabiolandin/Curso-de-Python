"""
Sistema de arquivos e navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo os.

os -> Operating System - Sistema operacional
"""
#Fazer o import
import os

#getcwd() -> pega o current work directory - diretório de trabalho recorrente
#Retorna o path (caminho) absoluto
print(os.getcwd())

#Para mudar o diretório podemos utilizar o chdir()
os.chdir('../..')

print(os.getcwd())

#Usuarios Windows
#Ter cuidado ao verificar diretórios
print(os.path.isabs('/'))

#Podemos identificar o sistema operacional com o módulo os NT = windows, posix = mac, linux
print(os.name)

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()
scanner = os.scandir()
arquivos = list(os.scandir())
print(arquivos)

print(arquivos[0].name) #Nome do arquivo
print(arquivos[0].path) #Caminho até o arquivo
print(arquivos[0].stat()) # Estatisticas sobre o arquivo
print(arquivos[0].is_dir()) #É um diretório? True

scanner.close()