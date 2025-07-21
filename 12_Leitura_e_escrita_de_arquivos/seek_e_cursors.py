"""
Seek e Cursors

seek() -> é utilizada para movimentar o cursor pelo arquivo.

Obs: quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo
no disco e do computador e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar
os trabalhos com o arquivos devemos fechar essa conexão. Para utilizarmos a função close()
"""
arquivo = open('texto.txt')
#print(arquivo.read())


#Movimentando o cursor pelo arquivo com a função seek() - recebendo parametro aonde deve ler
arquivo.seek(25)
#print(arquivo.read())

#redline() -. função que le o arquivo linha a linha
"""
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
"""

#readlines() ->
#print(arquivo.readlines())


#com a função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo
print(arquivo.read(50))

#Fechando a conexão com o arquivo
arquivo.close()

#Verifica se o arquivo foi fechado ou nao
print(arquivo.closed)

