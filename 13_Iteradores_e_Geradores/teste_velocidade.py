"""
Teste de Velocidade com Expressões Geradoras

# Generators (Geradores)

def nums():
    for num in range(1, 10):
        yield num

ge1 = nums()
print(ge1)
print(next(ge1))
print(next(ge1))

#Generators Expression
ge2 = (num for num in range(1, 10))

print(ge2)
print(next(ge2))
print(next(ge2))

"""
#Realizando o teste de velocidade
import time

#Generator Expression
gen_inicio = time.time()
print(sum(num for num in range(100000000)))
gen_tempo = time.time() - gen_inicio

#List Comprehension
list_inicio = time.time()
print(sum([num for num in range(100000000)]))
list_tempo = time.time() - list_inicio

print(f'O generator levou {gen_tempo} tempo')
print(f'O List comprehension levou {list_tempo} tempo')
