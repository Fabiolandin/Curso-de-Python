"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lóicoa e hierarquico
utilizando classes

Encapsular -> Cápsula

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
privados de usuário.
"""
class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de conta: {self.__saldo} com limite: {self.__limite}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo > valor:
            self.__saldo -= valor
        else:
            print('Saldo insuficiente')


#testando

conta1 = Conta('Geek', 150.00, 1500)

#print(conta1.titular)
#print(conta1.saldo)
#print(conta1.limite)

# Com os atributos publicos conseguimos alterar fácilmente os dados e manipular as classes
#conta1.saldo = 999999
#conta1.limite = 999999999

#COM OS ATRIBUTOS PRIVADOS - mét0do de burlar o private
print(conta1._Conta__titular)
conta1._Conta__titular = 'Fabio'
print(conta1._Conta__titular)

