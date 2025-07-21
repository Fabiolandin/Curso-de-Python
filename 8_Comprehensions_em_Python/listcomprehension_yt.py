"""
Passando a função para a list e rodando o for dentro do list_comprehension - básico
"""

def divisaodef (x,y):
    return x / y

def somadef(x,y):
    return x + y

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

divisao = [divisaodef(numero, 2) for numero in numeros]
soma = [somadef(numero, 2) for numero in numeros]

print(divisao)
print(soma)

"""
Aqui estamos filtrando os valores pares e o que for diferente de 6 continua igual else vira 600
"""
comdoisifs = [numero if numero != 6 else 600 for numero in numeros if numero % 2 == 0]
print(comdoisifs)

"""
Se o y for igual a 2 ele multiplica o y por 1000
"""
linhas_e_colunas = [(x, y) if y != 2 else (x, y *1000) for x in range(1, 4) for y in range(1, 4)]
print(linhas_e_colunas)

"""
Trasnformando a ultima letra dos nomes em letra maiuscula
exclui a ultima letra mas puxa o nome todo, pega a ultima letra e coloca em upper o restante é o looping
"""
nomes = ['fabio', 'rodrigo', 'michel', 'renato']
novos_nomes = [f'{nome[:-1] + nome[-1].upper()}' for nome in nomes]
print(novos_nomes)

"""
Definindo par e impar passando a lista par quando for par e impar segue o jogo normal
"""
listapareimpar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
parimpar = ['par' if numero % 2 == 0 else numero for numero in listapareimpar]
print(parimpar)


"""
Crie uma list comprehension que percorre uma string e substitui cada vogal por um "*".
"""
texto = "programacao"
conversor = ["*" if vogal in 'aeiou'else vogal for vogal in texto]
print(conversor)

"""
Dada uma lista de números, multiplique por 3 os ímpares e por 2 os pares, usando list comprehension. 
"""
numeros = [1, 2, 3, 4, 5]
multiplicador = [numero * 3 if numero % 2 != 0 else numero * 2 for numero in numeros]
print(multiplicador)

print("\n \n \n")

"""
Desafio 1 — Substituir pares e ímpares
Dada a lista de números de 1 a 10, crie uma nova lista que:
Substitua números pares por "par"
Substitua números ímpares por "ímpar"
"""
numeros = list(range(1, 11))
resultado = ["par" if numero % 2 ==0 else "Ímpar" for numero in numeros]
print(resultado)

"""
Desafio 2 — Substituir vogais por "*"
Dada a string "chatgpt":
Crie uma list comprehension que substitua as vogais por "*".
"""
texto = "chatgpt"
resultado = ["*" if letra in "aeiou" else letra for letra in texto]
print(resultado)

"""
Desafio 3 — Números positivos e negativos
Dada uma lista de números inteiros, retorne uma nova lista que:
Diga "positivo" se o número for maior que 0
Diga "negativo" se for menor que 0
Diga "zero" se for igual a 0
"""
numeros = [3, -1, 0, 7, -5]

resultado = ["zero" if numero == 0 else "positivo" if numero > 0 else "negativo" for numero in numeros]
print(resultado)

