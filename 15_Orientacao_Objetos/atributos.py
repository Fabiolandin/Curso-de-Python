"""
POO - Atributos

Atributos -> Representam as caracteristicas de um objeto. Ou seja, pelos atributos conseguimos representar
os estados de um objeto.

Em Python dividimos os atributos em 3 grupos:
    - Atributos de Instância
    - Atributos de Classe
    - Atributos Dinâmicos

# Atributos de instância: São atributos declarados dentro do mét0do construtor.
Significa que ao criarmos instancias/objetos de uma classe, todas as instancias terão esses atributos

Em python por convenção ficou estabelecido que t0do atributo de uma classe é publico, e pode ser acessado em tod0 o
projeto. Caso queira deixar privado usa-se __
"""
#Classes com atribudo de instancia publicos
class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

#Atributos publicos e atributos privados

#Aqui os métodos estão privados "__"
class Acesso:

    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

#Atributos de Classe - são atributos que são declarados diretamente na classe, ou seja, fora do costrutor.
#Atributos dinamico será exclusivo da instancia que o criou.