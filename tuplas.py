"""
Tuplas (tuple)

Tuplas são bem parecidas com listas, existem 2 diferenças bases:

1- As tuplas são representadas por parenteses (4,) e virgula ,
2- As tuplas são imutáveis: não podem ser mudadas, tota alteração em uma tupla gera uma nova tupla
3- As tuplas são mais rápidas do que as listas
4- Tuplas deixam seu código mais seguro

#Cuidado 1
tupla2 = (4) #isso não é uma tupla
tupla3 = (4,)

print(type(tupla2)) #isso não é uma tupla
print(type(tupla3))
"""

#Desempacotamento de tuplas
tupla = ('Fabio Tamburi Landin Junior', 'Pessoa Física')

nome, tipodepessoa = tupla

print(nome)
print(tipodepessoa)

#Métodos para adição e remoção de elementos nas tuplas não existem, porque tuplas são imutaveis

#Concatenaçãob de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) #Tuplas são imutaveis

print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2 #tuplas são imutaveis mas podemos sobrescrever seus valores
print(tupla1)

#Dicas na utilização de tuplas
#devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção

#Ex 1
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

#O acesso a elementos de uma tupla
print(meses[5])

#Verificando em qual indice o elemento esta na tupla
print(meses.index('Setembro'))