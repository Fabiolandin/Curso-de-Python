"""
mypy Checagem_de_tipos.py - vai falar possiveis erros

"""
#Programação em Python avançado
def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f"{texto.title()}".center(50, '#')

print(cabecalho('Geek University'))
print(cabecalho('geek university', alinhamento=False))
print(cabecalho('geek university', alinhamento=True))


#Programação em Python comum
def cabecalho(texto, alinhamento = True):
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f"{texto.title()}".center(50, '#')


"""
Vantagens de usar o Type Hinting
- Facilita encontrar erros
- Melhora a documentação do seu código
- Melhora as funcionalidades das IDES, autocomplete e etc

Desvantagens
- Estranhamento para programadores iniciantes
- Fazendo o usos de tipos temos uma ligeira queda de performance nos programas
"""

