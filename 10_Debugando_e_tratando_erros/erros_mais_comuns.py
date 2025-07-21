"""
Erros mais comuns em Python

É importante prestar atenção e aprender a ler as saidas de erros geradas pela execução do nosso código.

Os erros mais comuns:

SyntaxError -> Ocorre quando o python econtra um erro de sintax, voce escreveu algo que oi python não reconhece
como parte da linguagem.

Exemplos
a) def funcao:
       print("Geek University")

b) None = 1
   def = 1

NameError -> Ocorre quando uma variavel/função não foi definida.

Exemplos

a) print(geek)

b) geek()

TypeError -> Ocorre quando uma função/operação é aplicada a um tipo errado.

Exemplos

a) print(len(5))

b) print('Geek' + [])

IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um
indice inválido.

Exemplos

a)lista = ['Geek']
  print(lista[2])

b)lista = ['Geek']
  print(lista[0][10])

ValueError -> Ocorre quando uma função/operação built-in recebe um argumento com tipo correto mas valor inapropriado.

Exemplos

a) print(int('Geek'))

KeyError -> Ocorre quando tentamos acessar um dicionario com uma chave que não existe.

Exemplos

a)
dic = {'python': 'university'}
print(dic['geek'])

AtributeError -> Ocorre quando uma variavel não tem um atributo/função

Exemplos

a)
tupla = (11, 2, 31, 4)
print(tupla.sort())

IndententionError -> Erro de indentação

OBS: Exceptions e erros são sinonimos na programação.
"""
