"""
Estruturas Lógicas: and (e), or (ou), not (não, is (é)

Operadores unários:
    -not;
Operadores binários:
    -and, or, is

Regras de funcionamento:
para o 'and', ambos os valores precisam ser true
para o 'or', um ou outro precisa ser true
para o 'not' o valor do booleano é invertido
para o 'is' o valor é comparado com o segundo
"""

ativo = False
logado = True

if ativo and logado:
    print('Bem vindo')
else:
    print('Voce precisa ativar a sua conta')