"""
Escreva uma lambda que recebe um número e retorna seu quadrado
"""
calculo1 = lambda x: x*x
print(calculo1(55))

"""
Crie uma lambda que recebe nome e idade e retorna uma string no formato: "Nome: [nome], Idade: [idade]"
Teste com: ("Ana", 25), ("Carlos", 40)
"""
nomeidade = lambda nome, idade:f'Oi eu sou o/a {nome} e tenho {idade} anos'
print(nomeidade("Ana", 25))

"""
Escreva uma lambda que converte Celsius para Fahrenheit (F = C * 9/5 + 32)
Teste com: 0°C, 37°C, 100°C
"""
temperatura = lambda celsius: celsius * 9/5 + 32
print(temperatura(100))