"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe que passa a
herdar atributos e métodos da classe herdada.

OBS: Quando uma classe herda de outra classe, ela herda todos os atributos e métodos da classe herdada!

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
 - Super Classe
 - Classe Mãe
 - Classe pai
 - Classe base

Quando uma classe herda de outra classe, ela é chamada:
 - Sub Classe
 - Classe filha
 - Classe Específica

#Sobrescrita de mét0do, ocorre quando reescrevemos um métod0 presente na super classe em classes filhas
"""

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

class Cliente(Pessoa):
    """Cliente herda de pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.renda = renda

class Funcionario(Pessoa):
    """Funcionario herda de pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.matricula = matricula

    def nome_completo(self):
        return f'Funcionario: {self.matricula} Nome: {self.nome}'


cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '123.999.785-42', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
