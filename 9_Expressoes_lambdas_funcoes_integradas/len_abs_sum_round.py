"""
#len
len() -> Retorna o tamanho (ou seja, o número de itens) de um iteravel.

abs() -> retorna o valor absoluto de um numero inteiro ou real

sum() -> recebe como parametro um iteravel, podendo receber um valor inicial e retorna a soma total dos elementos

round() -> retorna um numero arredondado para um n digito de precisão, se n for informado o número retorna o inteiro
mais próximo da entrada.
"""
#len
print(len('Fabio Tamburi Landin'))
print(len([1, 2, 3, 4, 5, 6]))

#abs
print(abs(-5))
print(abs(5))
print(abs(-3.14))
print(abs(3.14))

#Sum
print(sum([1, 2, 3, 4, 5, 6]))
print(sum([1, 2, 3, 4, 5, 6], -5))

#Round
print(round(3.14))
print(round(1.22221499999, 2)) #duas casas decimais
print(round(1.29999999, 2))
