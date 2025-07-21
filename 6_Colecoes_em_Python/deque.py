"""
Módulo Collections - Deque
Podemos dizer que o deque é uma lista de alta performance.


"""
#Importanto deque
from collections import deque

#Criando deques
deq = deque('Fabio')
print(deq)

#Adicionando elementos no deque
deq.append(' Junior')
print(deq)

#Adicionando na esquerda
deq.appendleft('1 ')
print(deq)

# Remover elementos
print(deq.pop())
print(deq)

print(deq.popleft())
print(deq)

