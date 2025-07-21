"""
Geradores
-Geradores(Generators) são iteradores (iterators)

OBS: O contrário não é verdadeiro. Ou seja, nem  td iterator é um gerador

Outras informações:
- Generators podem ser criados com funções geradoras
- Funções geradores utilizam a palavra reservada yield
- Generators podem ser criados com Expressões Geradoras
Diferença entre funções e generator funcitons

Funções
Utilizam return
retorna uma vez
quando executada, retorna um valor

Generator function
Utilizam Yield
podem utilizar yiel multiplas vezes
quando executada, retorna um generator
"""

#Exemplo Generator Function

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

#Obs: uma generator function GERA um generator

gen = conta_ate(5)

print(type(gen))
