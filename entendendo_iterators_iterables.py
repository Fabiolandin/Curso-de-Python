"""
Entendendo Iterators e Iterables

Iterator ->
    - Objeto que pode ser iterado.
    - Objeto que retorna um dado, sendo um elemento por vez quando uma func next() é chamada

Iterable ->
     - Objeto que ira retornar um iterator quando a função iter() for chamada
     - É qualquer objeto que vc pode percorrer com um for ou passar para funcs como list()/sorted()/map()/filter() etc.
"""
nome = 'Fabio' #é um iterable mas não é um iterator
numeros = [1, 2, 3, 4, 5] #é um iterable mas não é um iterator

it1 = iter(nome)
it2 = iter(numeros)

#print(next(it1))

for letra in nome:
    print(letra)
