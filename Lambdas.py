"""
Utilizando Lambdas

Conhecidas por expressões lambdas, ou simplesmente lambdas, são funções sem nome, ou seja, funções anonimas.

Lambdas são usadas para coisas mais simples, sem muitas linhas e complexidade sendo assim melhor que func para o caso.
"""
#Função em python
def funcao(x):
    return 3 * x + 1

print(funcao(4))

#Exemplo de lambda
lambda x: 3 * x + 1


#como utilizar a axpressão lambda - forma menos comum
calc = lambda x: 3 * x + 1
print(calc(4))

#Podemos ter expressões lambdas com multiplas entradas
nome_copleto = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_copleto(' angeliNa', 'JoliE'))
print(nome_copleto(' FABIO', 'lanDIN'))

#Outro exemplo - ordenando por ordem alfabetica do ultimo nome
autores = ['Isaac Asimov', 'Ray Mac Bradbury', 'Robert Heinlein', 'Amanda Clark', 'Marcos Silva Junior', 'Fernanda Dopez']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)
