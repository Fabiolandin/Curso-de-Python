import math

# math.prod - retorna o produto de um container numérico
nuns_v1 = [2, 3, 6, 8]
nuns_v2 = (2, 3, 6, 8)
nuns_v3 = {2, 3, 6, 8}

print(math.prod(nuns_v1))
print(math.prod(nuns_v2))
print(math.prod(nuns_v3))
print('\n')

"""
2 * 3 * 6 * 8 -> 288
"""

# math.isqrt - retorna a parte inteira da raiz quadrada de um número

print(math.isqrt(9))
print(math.sqrt(9))

print(math.isqrt(17))
print(math.sqrt(17))

# math.dist - retorna a distância euclidiana entre dois pontes, 3D ou 2D

# Pontos 3D
p3d1 = (12, 50, 40)
p3d2 = (6, 7, 13)

# Pontos 2D
p2d1 = [12, 50]
p2d2 = [6, 7]

print(math.dist(p3d1, p3d2))
print(math.dist(p2d1, p2d2))