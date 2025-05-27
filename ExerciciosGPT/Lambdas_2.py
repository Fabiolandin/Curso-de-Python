"""
Calculadora Dinâmica
Crie uma função que retorna um dicionário de operações matemáticas usando lambdas. O dicionário deve conter as seguintes
operações para dois números: soma, subtração, multiplicação, divisão, potência e módulo.
"""
calculadora = lambda: {
    'soma': lambda x, y: x + y,
    'subtracao': lambda x, y: x - y,
    'multiplicacao': lambda x, y: x * y,
    'divisao': lambda x, y: x / y,
    'potencia': lambda x, y: x ** y,
    'modulo': lambda x, y: x % y
}
operacoes = calculadora()

# Teste
print(operacoes['soma'](10, 5))         # 15
print(operacoes['divisao'](10, 2))      # 5.0
print(operacoes['potencia'](2, 3))      # 8
print(operacoes['modulo'](10, 3))       # 1

"""
Crie uma lista apenas com os números pares de uma lista original usando lambda e filter.
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtro = filter(lambda num: num % 2 == 0, numeros)
print(list(filtro))


"""
Use map() com lambda para converter uma lista de preços em uma lista com 10% de desconto.
"""
precos = [100, 250, 80, 300]

def conversor(lista):
    return lista * 0.9

desconto = map(conversor, precos)
print(list(desconto))

"""
Ordene uma lista de produtos pelo preço usando lambda como key.
"""
produtos = [
   {'nome': 'Notebook', 'preco': 2500},
   {'nome': 'Mouse', 'preco': 50},
   {'nome': 'Monitor', 'preco': 800}
]
produtos.sort(key=lambda produto: produto['preco'])
print(produtos)

"""
Crie uma função chamada operacao que recebe uma string ("soma", "subtracao", "multiplicacao" ou "divisao") e retorna 
uma lambda correspondente à operação.
"""
def operacao(tipo):
    if tipo == "soma":
        return lambda x, y: x + y
    elif tipo == "subtracao":
        return lambda x, y: x - y
    elif tipo == "multiplicacao":
        return lambda x, y: x * y
    elif tipo == "divisao":
        return lambda x, y: x / y

soma = operacao("soma")           # retorna lambda x, y: x + y
print(soma(10, 5))                # imprime 15

div = operacao("divisao")        # retorna lambda x, y: x / y
print(div(10, 2))                 # imprime 5.0


