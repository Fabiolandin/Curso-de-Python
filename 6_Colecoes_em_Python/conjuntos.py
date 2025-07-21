"""
Conjuntos

- Conjuntos em python é uma referencia a teoria dos conjuntos matematica.

- Em python são chamados de Sets, e não possuem valores duplicados e nem ordenados.
"""

#Definindo um conjunto

# Forma 1
s = set({1, 2, 3, 4, 5, 1, 2, 3})

print(s)
print(type(s))

#OBS: ao criar um conjunto caso seja adicionado um valor ja existente, o mesmo será ignorado sem gerar
# error e não fará parte do conjunto


#Conjunto podemos colocar todos os tipos de dado
s1 = {1, 'b', True, 32.5}
print(s1)
print(type(s1))

for valor in s1:
    print(valor)

#Usos interessantes com sets

# Formulario de cadastro
cidades = ['Belo Horizonte', 'São Paulo', 'Belo Horizonte', 'Cuiaba', 'Birigui', 'Araçatuba', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

#Precisamos saber quantas cidades distintas temos.
print(len(set(cidades)))


#Adicionando elementos em um conjunto / Duplicidade n gera erro, só não adiciona.
s = {1, 2, 3, 4}
s.add(5)
print(s)

#Removendo elementos

# Forma 1
s.remove(3)
print(s)

# Forma 2 - SE O VALOR NÃO FOR ENCONTRADO NENHUM ERRO É GERADO
s.discard(2)
print(s)

#Copiando um conjunto para outro
# Forma 1 - Deep copy
novo = s.copy()
print(novo)

novo.add(6)
print(novo)
print(s)

#Removendo todos os itens do conjunto
s.clear()
print(s)


# Métodos matematicos de conjuntos
# Imagina que temos 2 conjuntos, um com estudantes de python e um estudantes de java

estudantes_python = {'Marcos', 'Julia', 'Fernando', 'Gabriel', 'Fabio', 'Carlos'}
estudantes_java = {'Ellen', 'Marcos', 'Carlos', 'Bruno', 'Rodrigo', 'Fabio'}

#Precisamos gerar um conjunto com nomes de estudantes unicos

# Forma 1 - Utilizando union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

#Forma 2 - utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

#Gerando o conjunto dos que estão cursando os dois cursos

# Forma 1 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

#Estudantes que estao em um e não estão no outro
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)