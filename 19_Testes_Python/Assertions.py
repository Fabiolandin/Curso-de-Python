"""
Assertions (Afirmações/Checagens/Questionamentos)

Em python utilizamos a palavra reservada 'assert' para realizar simples afirmações
realizadas nos testes.

Utilizamos o 'assert' em uma expressão que queremos checar se é valida ou não
se a expressão for verdadeira o 'asser' retorna none, caso seja falsa levanta um erro do tipo
AssertionError.

#Obs: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizada

#Obs: A palavra 'assert' pode ser utilizada em qualquer função ou código, nosso .... não precisa ser exclusivamente
nos testes

# Alerta: CUIDADO AO UTILIZAR O 'ASSERT'
Se um programa python for executado com um parametro -O, nenhum assertion será executado.
"""

def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b

#ret = soma_numeros_positivos(2, 4) # 8
#ret = soma_numeros_positivos(2, 4) # AssertionError
#print(ret)

def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'bata frita',
        'cachorro quente',
    ], 'A comida precisa ser fastfood'
    return f'Eu estou comendo a {comida}'

comida = 'pizza'
print(comer_fast_food(comida))
comida = 'macarrao'
print(comer_fast_food(comida))


