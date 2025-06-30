"""
Json e Pickle

JSON -> JavaScript Object Notation

API -> meios de comunicação entre os serviços oferecidos por empresas e o cliente (PONTE)
"""
import json

#ret = json.dumps(['produto', {'Playstation 4': ('2TB', 'Novo', '220V', 3500)}])

#print(type(ret))
#print(ret)

#Integrando json com pickle - ESCREVENDO EM ARQUIVOS JSON
import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

#felix = Gato('Felix', 'Tazian')

#with open('felix.json', 'w', encoding='utf8') as arquivo:
   # ret = jsonpickle.encode(felix)
   #arquivo.write(ret)

#lendo arquivos json
with open('felix.json', 'r', encoding='utf8') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.encode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)

