"""
POO - Métodos Mágicos

Métodos Mágicos, são todos os métodos que utilizam dunder.

dunder init -> __init__

dunder repr -> Representação do objeto
    def __repr__(self):
        return f'{self.__titulo} escrito por {self.__autor} com {self.__paginas} paginas'

    def __str__(self):
        return f'{self.__titulo} escrito por {self.__autor} com {self.__paginas} paginas'
"""
class Livro:

    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    def __len__(self):
        return self.__paginas


livro =  Livro('Python Rocks!', 'Geek University', 400)
livro1 = Livro('Python e IA!', 'Geek University', 560)

print(livro)
print(livro1)

print(len(livro))
print(len(livro1))