"""
Teste de Memória com Generators

# Sequencia de Fibonacci
1, 1, 2, 3, 5, 8, 13
"""
#função usando lista
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

#Teste - 449mb
#for n in fib_lista(100000):
 #   print(n)

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield contador
        contador = contador + 1

#Teste 2 - Geradores 3MB
for n in fib_gen(100000):
    print(n)