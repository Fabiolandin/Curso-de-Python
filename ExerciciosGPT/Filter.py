"""
Filtrando Números Pares
Dada a lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], use filter() para:
a) Filtrar números pares
b) Filtrar números maiores que 5
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = filter(lambda n: n % 2 == 0, lista)
print(list(resultado))

resultado2 = filter(lambda n: n > 5, lista)
print(list(resultado2))

"""
Filtrando Strings Vazias
Dada a lista ["Python", "", "Java", "C++", "", "JavaScript"], filtre as strings vazias
"""
lista2 = ["Python", "", "Java", "C++", "", "JavaScript"]
resultado3 = filter(lambda n: len(n) > 0, lista2)
print(list(resultado3))

"""
Dada a lista de produtos:
Use filter() para:
a) Filtrar produtos com preço > 100
b) Filtrar produtos que começam com "M"
"""

produtos = [
    {"nome": "Notebook", "preco": 2500},
    {"nome": "Mouse", "preco": 50},
    {"nome": "Teclado", "preco": 100},
    {"nome": "Monitor", "preco": 800}
]

resultado4 = filter(lambda produto: produto['preco'] > 100, produtos)
resultado5 = filter(lambda produto: produto['nome'][0] == 'M', produtos)

print(list(resultado4))
print(list(resultado5))

