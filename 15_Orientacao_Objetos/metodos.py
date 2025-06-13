"""
POO - Métodos

- Métodos (Funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode
realizar no seu sistema.

Em Python, dividimos os métodos, em 2 grupos: Métodos de instancia e Métodos de Classe

# Métodos de instancia.
# O metodo dunder init __init__ é um metodo especial chamado de construtor e sua função é
construir o objeto a partir da classe.
"""

class Lampada:
    def __index__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

p1 = Produto('Playstation 4', 'Video Game', 2300)

print(p1.desconto(50))

user1 = Usuario('Fabio', 'Landin', email='flandin1990@gmail.com', senha='12345')
user2 = Usuario('Flavia', 'Regina', email='flacarvalho@gmail.com', senha='12345')

print(user1.nome_completo())
print(user2.nome_completo())
print(Usuario.nome_completo(user1))

#Métodos Privados - só são executados dentro da classe e são iniciados com __

