"""
POO - Herança Múltipla

Herança Múltipla nada mais é que a possibilidade de uma classe herdar de múltiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

#Obs: A herança multipla pode ser feita de duas maneiras:
 - Por Multiderivação direta
 - Por Multiderivação Indireta

#Obs não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará
todos os atributos e métodos da super classe.
"""
class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)


baleia = Aquatico('Baleia')

print(baleia.cumprimentar())
print(baleia.nadar())

tatu = Terrestre('Tatucaminhadentro')
print(tatu.cumprimentar())
print(tatu.andar())

ping = Pinguim('Pinguim')
print(ping.cumprimentar())
print(ping.andar())
print(ping.nadar())

#Objeto é instancia de ....
print(f'ping é instancia de pinguim? {isinstance(ping, Pinguim)}')
print(f'ping é instancia de terrestre? {isinstance(ping, Terrestre)}')
print(f'ping é instancia de aquatico? {isinstance(ping, Aquatico)}')
print(f'ping é instancia de Animal? {isinstance(ping, Animal)}')