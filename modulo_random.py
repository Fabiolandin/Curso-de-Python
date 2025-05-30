"""
Módulo Random e o que são módulos?

- Em Python, módulos nada mais são que outros arquivos em python.

Módulo Random -> possui várias funções para geração de números pseudo-aleatório.
"""
#Obs: Existem duas formas de se utilizar um modulo ou função deste

#Forma 1 - Importando t0do o módulo
import random

#Ao realizar o import de td o módulo, todas as funções, atributos, classes que estiverem dentro do modulo
# ficarão em memória, e não seria uma forma ideal de utilização.

print(random.random())

#Obs não confunda a função random com pacote random, a random é apenas uma função dentro do módulo random

#Forma 2 - Importando uma função especifica do módulo
from random import random

for i in range(5):
    print(random())

#No import acima estamos falando "no módulo random impor a função random"

#Uniform -> gera um numero pseudo-aleatório entre os valores estabelecidos
from random import uniform

for i in range(3):
    print(uniform(3, 7)) # 7 não é incluído.

# radint() -> gera valores pseudo-aleatórios entre os valores estabelecidos.
from random import randint

#Geraror de apostas da mega-sena
for i in range(6):
    print(randint(0, 61), end=', ')

print("\n")

#choice() -> Mostra um valor aleatório entre um iteravel
from random import choice
jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))

#Shuffle() -> função de embaralhar dados
from random import shuffle
cartas = ['Q', 'J', 'K', 'A', '2', '3', '4', '5']
shuffle(cartas)
print(cartas)
