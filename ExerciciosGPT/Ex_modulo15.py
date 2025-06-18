"""
Crie um sistema de Home Theater com as seguintes classes:
1. AparelhoSom:
- Atributos: status (ligado/desligado), volume (0-100), modo (normal/rock/pop/jazz)
- Métodos: ligar/desligar, aumentar/diminuir volume, mudar modo

2. Projetor:
- Atributos: status, brilho (0-100), entrada (HDMI/VGA/USB)
- Métodos: ligar/desligar, ajustar brilho, mudar entrada

3. ControleUniversal:
- Deve controlar ambos os aparelhos (AparelhoSom e Projetor)
- Implemente métodos para:
  * Ligar/desligar t0do o sistema
  * Ajustar volume e brilho simultaneamente
  * Definir cena predefinida (ex: "cinema" ajusta som e imagem)
"""

class AparelhoSom:

    def __init__(self):
        self.__status: bool = False
        self.__volume: int = 50
        self.__modo = "normal"

    @property
    def status(self) -> bool:
        return self.__status

    @status.setter
    def status(self, status: bool) -> None:
        self.__status = status

    @property
    def volume(self) -> int:
        return self.__volume

    @volume.setter
    def volume(self, volume: int) -> None:
        self.__volume = volume

    @property
    def modo(self) -> str:
        return self.__modo

    @modo.setter
    def modo(self, modo: str) -> None:
        self.__modo = modo

    def ligar(self):
        self.__status: bool = True
        print('O Aparelho de som foi ligado')

    def desligar(self):
        self.__status: bool = False
        print('O Aparelho de som foi desligado')

    def aumentarVolume(self) -> None:
        self.volume = self.volume + 10
        print(f'Volume aumentado para: {self.volume}')

    def diminuirVolume(self) -> None:
        self.volume = self.volume - 10
        print(f'Volume diminuido para: {self.volume}')


class Projetor:

        def __init__(self):
            self.__status: bool = False
            self.__brilho: int = 50
            self.__entrada: str

        @property
        def status(self) -> bool:
            return self.__status

        @status.setter
        def status(self, status: bool) -> None:
            self.__status = status

        @property
        def brilho(self) -> int:
            return self.__brilho

        @brilho.setter
        def brilho(self, brilho: int) -> None:
            self.__brilho = brilho

        def ligar(self):
            self.__status: bool = True
            print('O Projetor foi ligado')

        def desligar(self):
            self.__status: bool = False
            print('O Projetor foi desligado')

        def aumentar_brilho(self) -> None:
            self.brilho = self.brilho + 10
            print(f'Brilho aumentado para: {self.brilho}')

        def diminuir_brilho(self) -> None:
            self.brilho = self.brilho - 10
            print(f'Brilho aumentado para: {self.brilho}')

class ControleUniversal:
    def __init__(self, aparelhosom: AparelhoSom, projetor: Projetor) -> None:
        self.__aparelhosom = aparelhosom
        self.__projetor = projetor

    @property
    def aparelhosom(self) -> AparelhoSom:
        return self.__aparelhosom

    @property
    def projetor(self) -> Projetor:
        return self.__projetor

    def ligar(self) -> None:
        self.__aparelhosom.ligar()
        self.__projetor.ligar()
        print('Sistema completo desligado \n')

    def desligar(self) -> None:
        self.__aparelhosom.desligar()
        self.__projetor.desligar()
        print('Sistema completo desligado')

    def aumentar_brilho_e_volume(self) -> None:
        self.__aparelhosom.aumentarVolume()
        self.__projetor.aumentar_brilho()
        print('Volume e brilho aumentado')

    def diminuir_brilho_e_volume(self) -> None:
        self.__aparelhosom.diminuirVolume()
        self.__projetor.diminuir_brilho()
        print('Volume e brilho diminuido')



if __name__ == "__main__":
    ap: AparelhoSom = AparelhoSom()
    pr: Projetor = Projetor()

    cr: ControleUniversal = ControleUniversal(ap, pr)
    cr.ligar()
    cr.desligar()
    cr.aumentar_brilho_e_volume()






