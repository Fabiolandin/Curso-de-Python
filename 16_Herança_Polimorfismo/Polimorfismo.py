"""
POO - Polimorfismo

Poli -> Muitas
Morfis -> Formas

Quando re-implementamos o métod0 presenta na classe pai em classes filhas, estamos realizando
uma sobrescrita de mét0do (Overriding)

O Overriding é a melhor representação do polimorfismo.
"""

class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A Classe filha precisa implementer este método')

    def comer(self):
        print(f'{self._Animal__nome} esta comendo...')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala au au au')

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau miau')

class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fiti fiti fiti')

#Testes
felix = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()