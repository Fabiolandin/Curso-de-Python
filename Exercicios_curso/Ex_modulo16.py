"""
Crie a classe Veiculo, contendo marca e modelo. Crie as propriedades getters e setters para os atributos e
um mét0do para imprimir os dados de um veículo. Crie também o construtor da classe.
"""
class Veiculo:

    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    def imprimir(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}')

carro = Veiculo('Ford', 'Amarok')
carro.imprimir()


"""
Crie a classe Carro que herda a classe Veiculo e possui o atributo portas. Crie as propriedades getters e
setters para o atributo. Crie também o construtor da classe. Sobrescreva o método de imprimir os dados do
veículo de forma a apresentar também a quantidade de portas do carro.
"""
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.__portas = portas

    @property
    def porta(self):
        return self.__portas

    @porta.setter
    def porta(self, porta):
        self.__portas = porta

    def imprimir(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Portas {self.__portas}')

carro2 = Carro('Ford', 'Amarok', 4)
carro2.imprimir()

"""
Crie um programa, instancie um objeto da classe Carro e teste o seu médodo.
"""

if __name__ == "__main__":

    cr = Carro('Audi', 'A8', 2)
    cr.imprimir()
