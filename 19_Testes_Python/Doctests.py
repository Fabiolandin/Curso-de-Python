"""
Doctests


Doctests são testes que colocamos na docstring das funções/métodos Python.

Para rodar um test do doctest:
python -m doctest -v nome_do_modulo

Dentro do doctest, o python não reconhece string com aspas duplas. Precisa ser aspas simples.
"""


def soma(a, b):
    """Soma os números a e b

    >>> soma(1, 2)
    3
    """
    return a + b

print(soma(3, 4))

#Outro exemplo aplicando o TDD

def duplicar(valores):
    """Duplica os valores em uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (most recent call last):
       ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]
