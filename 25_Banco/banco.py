from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas:list[Conta] = list()

def main() -> None:
    print('================================================')
    print('=================== Landinho ===================')
    print('===================== Bank =====================')
    print('================================================')

    print('Selecione uma opção no menu: ')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Efetuar transferência')
    print('5 - Lista contas')
    print('6 - Sair do sistema')

    opcao: int = int(input(''))

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte sempre')
        sleep(2)
        exit(0)
    else:
        print('Opção invalida')
        sleep(2)
        menu()





def menu() -> None:
    pass


def criar_conta() -> None:
    print('Informe os dados do cliente: ')

    nome = input('Nome do cliente: ')
    email = input('Email do cliente: ')
    cpf = input('CPF do cliente: ')
    data_nascimento = input('Data de nascimento do cliente: ')

    cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)
    contas.append(conta)

    print('Conta criada com sucesso!')
    print('Dados da conta: ')
    print('===========================')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))

            conta.sacar(valor)
        else:
            print(f'Ainda não foi encontrada a conta de número {numero}')
    else:
        print('Ainda não existem contas cadastradas!')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))
        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor: float = float(input('Informe o valor do saque: '))

            conta.depositar(valor)
        else:
            print(f'Não foi encontrada uma conta com número {numero}')
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('Informe o número da sua conta: '))

        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input('Informe o número da conta destino: '))
            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input('Informe o valor da trasnferencia: '))

                conta_o.transferir(conta_d, valor)
            else:
                print(f'A conta destino com número {numero_d} não foi encontrada.')
        else:
            print(f'A conta com número {numero_o} não foi encontrada.')

    else:
        print('Ainda não existem pessoas com contas cadastradas')
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Lista de contas cadastradas:')

        for conta in contas:
            print(conta)
            print('========================')
            sleep(1)
        else:
            print('Não existe contas cadastradas')
        sleep(2)
        menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()
