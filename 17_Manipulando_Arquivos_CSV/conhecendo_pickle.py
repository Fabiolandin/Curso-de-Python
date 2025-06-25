"""
Conhecendo o Pickle

A função do Pickle é realizar o seguinte processo:

Objeto Python -> Binarização
Binarização -> Objeto Python

Este processo é chamado de serialização/deserialização

#OBS: o módulo picke não é seguro contra arquivos maliciosos e desta forma não é recomendado
trabalhar com arquivos pickle de pessoas ou fontes desconhecidas
"""
import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.nome} está comendo')

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def miao(self):
        print(f'{self.nome} está miando')

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} está latindo')


"""
#fazendo a escrita em arquivos pickle
felix = Cachorro('Felix')
pluto = Gato('Pluto')

with open('animais.pickle', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)
"""

#Fazer a leitura de arquivos pickle
with open('animais.pickle', 'rb') as arquivo:
    cachorro, gato = pickle.load(arquivo)
    print(f'O gato chama-se {gato.nome}')
    gato.miao()

    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()