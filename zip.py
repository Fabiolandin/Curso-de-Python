"""
Zip

zip() -> Cria um iterável (Zip Object) que agrega elemente de cada um dos iteraveis passados como entrada em pares.
"""
# Exemplos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)
print(zip1)
print(type(zip1))

#Sempre podemos gerar uma Lista, Tupla, ou Dicionário

print(list(zip1))
print(tuple(zip1))
print(set(zip1))
print(dict(zip1))

#O zip utiliza como parametro o menor tamanho em iterável. Isso significa que se estiver trabalhando com iteraveis de
#tamanhos diferentes ira parar quando o elemento de menor tamanho acabar.

lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))

#Lista de tuplas

dados = [(0, 1), (2, 3), (4, 5)]
print(list(zip(*dados)))

#Achando a maior nota do aluno.
#Exemplos mais complexos
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Pedro', 'Fabio']

#Enxegando melhor
zip5 = zip(prova1, prova2, alunos)
print(list(zip5))

#Separando a maior nota de cada aluno
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))
