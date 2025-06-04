"""
StringIO

Atenção: para ler ou escrever dados em arquivos do sistema operacional o software precisa ter permissão.
-Permissão de leitura
-Permissão de escrita.

StringIO -> Utilizado para ler e criar arquivos em memória
"""
#Primeiro fazemos o import
from io import StringIO

mensagem = 'Essa é apenas uma string normal'

#Podemos criar um arquivo em memória ja com uma string insertida ou mesmo vazio para inserirmos textos depois
arquivo = StringIO(mensagem)

#Agora tendo o arquivo, podemos utilizar tudo que ja sabemos.
print(arquivo.read())

arquivo.write(' Outro texto ')

#Podemos movimentar o cursor
arquivo.seek(0)

print(arquivo.read())