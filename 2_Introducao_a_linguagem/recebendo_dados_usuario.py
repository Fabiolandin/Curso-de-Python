"""
Recebendo dados do usuário

To do dado recebido via INPUT é do tipo string
"""
# Entrada de dados
print("Qual seu nome? ")
nome = input()

#exemplo de print antigo
print('Seja bem vindo(a) {0}'.format(nome))

print("Qual sua idade?")
idade = input()

# Processamento

#exemplo de print antigo
print("O(a) {0} tem {1} anos".format(nome, idade))

#Exemplo de print atual
print("----------------------------------------------")
print(f'Seja bem vindo(a) {nome} você tem {idade} anos')
print(f'O {nome} nasceu em {2025 - int(idade)}')