"""
Leitura de Arquivos

Para ler um arquivo em python, utilizamos a função integrada open()

open() -> Na forma mais simples de utilização nós passamos apenas um parametro de entrada
que é o nome do arquivo a ser lido. e retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

OBS: por padrão a função open abre o arquivo para leitura, se o arquivo n existir retorna o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
mode r -> Modo de leitura. r -> read() -> ler
"""

#Exemplo
arquivo = open('texto.txt')

#print(arquivo)
#print(type(arquivo))

ret = arquivo.read()

print(type(ret))
print(ret)

#Para ler o conteudo de arquivo após sua abertura, devemos utilizar a sua função read()
print(arquivo.read())

#o python, utiliza um recurso para trabalhar com arquivos chamado cursor.
#esse cursor, funciona como o cursor quando estamos escrevendo.