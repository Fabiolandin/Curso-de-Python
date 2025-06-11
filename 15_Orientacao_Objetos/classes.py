"""
POO - Classes

Em POO, Classes nada mais são que modelos dos objetos do mundo real sendo representados computacionalmente.

Imagina que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:
    - Atributos -> Representam as caracteristicas do objeto. Ou seja pelos atributos conseguimos representar
    os estados de um objeto. No caso da lampada, possivelmente iriamos querer saber se é 110 ou 220, se é branca e etc.

    - Métodos (funções) -> Representam os comportamentos do objeto. OU seja, as ações que este objeto pode realizar,
    no caso da lampada exemplo: ligar, desligar, mudar de cor

Em Python para definir uma classe utilizamos a palavra reservada class.

OBS: Utilizamos a palavra 'pass' em Python quando temos um bloco de código que ainda não está implementado.
OBS: Quando nomeamos uma classe em Python utilizamos por convenção o nome com inicial em maiusculo, se o nome
for composto, utiliza-se as iniciais de ambas as palavras em maiúsculo, todas juntas.
"""

class Lampada:
    pass

lamp = Lampada()
print(type(lamp))