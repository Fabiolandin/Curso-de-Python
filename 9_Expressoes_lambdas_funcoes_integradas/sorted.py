"""
Sorted

Obs: Apesar do nome n é igual a função sort(), o sorted() só funciona em listas.

Podemos utilizar o sorted() com qualquer iteravel.

Ele server para ordenar elementos, porém ele n modifica a lista.
"""

#Exemplo
numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros))
print(numeros)

#Adicionando parametros ao sorted()
print(sorted(numeros, reverse=True))

#Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "Fabio", "tweets": ["Eu amo cachorros", "Eu adoro lanches artesanais"]},
    {"username": "Samuel", "tweets": []},
    {"username": "Leandro", "tweets": ["Eu amo gatos", "Eu adoro pizzas"]},
    {"username": "Renato", "tweets": ["Eu meus gatinhos", "Eu adoro Açai"]},
    {"username": "Carlos", "tweets": []}
]

print(usuarios)
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

