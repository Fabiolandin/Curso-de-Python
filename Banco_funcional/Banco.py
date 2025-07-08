"""
Sistema Bancario em POO
Saque
Deposito
Extrato
"""

menu = """
    Saque    [S] 
    Deposito [D] 
    Extrato  [E]
    Sair     [Q]
"""
escolha = []
saldo = 0
valor = 0
extrato = []
saques_realizados = 0
limite_saque = 3

while True:
    print(menu)
    print('Saldo: R$ {:.2f}'.format(saldo))
    escolha = input('Qual operação deseja realizar?: ')

    #Saque
    if escolha == 'S' or escolha == 's':
        valor = int(input('Quanto deseja sacar?: '))
        if valor <= saldo and saques_realizados < limite_saque:
            saldo = saldo - valor
            extrato.append(f'Saque: {valor}')
            saques_realizados = saques_realizados + 1
            print(saques_realizados)
        else:
            print('Saldo insuficiente, ou limite de saques já atingidos. ')

    #Deposito
    elif escolha == 'D' or escolha == 'd':
        valor = int(input('Quanto deseja depositar?: '))
        saldo = saldo + valor
        extrato.append(f'Deposito: {valor}')

    #Extrato
    elif escolha == 'E' or escolha == 'e':
        print('x==== Extrato ====x')
        if len(extrato) == 0:
            print('Nenhuma movimentação nessa conta')
        else:
            for operacao in extrato:
                print(operacao)
            print('\n')
            print('Saldo: R$ {:.2f}'.format(saldo))

    elif escolha == 'Q' or escolha == 'q':
        print('\n')
        print('Saldo: R$ {:.2f}'.format(saldo))
        break
