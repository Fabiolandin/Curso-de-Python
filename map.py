"""
Map
Com map, fazemos mapeamento de valores para função.
"""
import math

def area(r):
    """Calcula a área de um circulo com raio 'r' """
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2, 5, 7,1, 0.3, 10, 44]

#Forma comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Forma 2 - Map
#Map é uma função que recebe dois parametros: O primeiro a função, e o segundo um iteravel. Retorna um map objetc

areas = map(area, raios)

print(areas)
print(type(areas))

print(list(areas))

# Forma 3 - Map com lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

#Ultimo Exemplo
cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Brasil', 33)]
print(cidades)

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))