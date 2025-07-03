"""
Por que testar nosso código?
 - Reduzir bugs
 - Testes garantem que novos recursos da sua aplicação não quebrem recursos antigos.
 - Testes garantem que bugs que foram corrigidos anteriormente continuam corrigidos.
 - Testes garantem que a refatoração que costumamos a fazer não tragam novos bugs(problemas).

 TDD - Test Driven Developtment (desenvolvimento guiado por testes)

Com TDD é utilizado estágios de desenvolvimento:
 - Você escreve seu teste primeiro.
 - Então voce descreve o código minimo suficiente para fazer o teste passar
 - Então refatora o código para realizar a funcionalidade e testa novamente.


Testes Automatizados!

"""

class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando')

felix = Gato('Felix')
felix.miar()
print(felix.nome)