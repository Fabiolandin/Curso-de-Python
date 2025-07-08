"""
Sistema Bancario em POO
Saque
Deposito
Extrato
"""

class Menu:
    def __init__(self):
        menu = """
            Saque    [S] 
            Deposito [D] 
            Extrato  [E]
            Sair     [Q]
        """
        print(menu)


class ContaBancaria:
    def __init__(self):
        self.saldo = 0  # Atributo da classe (estado permanente)
        self.extrato = []
        self.limitesaque = 3
        self.saquediario = 0

    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente')
        elif valor <= 0:
            print('O valor de saque deve ser positivo!')
        elif valor > 500:
            print('O limite máximo por saque é R$ 500,00')
        elif self.saquediario >= self.limitesaque:
            print('Limite de saque díario atingido')
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R${valor:.2f}")
            print(f'Saldo: R$ {self.saldo:.2f}')
            self.saquediario += 1

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Deposito: R${valor:.2f}")
            print(f'Saldo: R$ {self.saldo:.2f}')
        else:
            print("Você não pode depositar valores negativos!")

    def ver_extrato(self):
        print('x==== Extrato ====x')
        if len(self.extrato) == 0:
            print('Nenhuma movimentação nessa conta')
        else:
            for operacao in self.extrato:
                print(operacao)
            print('x==== Fim de Extrato ====X')
            print(f'Saldo: R$ {self.saldo:.2f}')


class Banco:
    def __init__(self):
        self.conta = ContaBancaria()

    def executar(self):
        while True:
            Menu()
            escolha = input('Qual operação deseja realizar?: ')
            if escolha == 'S' or escolha == 's':
                valor = int(input('Quanto você deseja sacar?'))
                self.conta.sacar(valor)
            elif escolha == 'D' or escolha == 'd':
                valor = int(input('Quanto você deseja depositar?'))
                self.conta.depositar(valor)
            elif escolha == 'E' or escolha == 'e':
                self.conta.ver_extrato()
            elif escolha == 'Q' or escolha == 'q':
                break


if __name__ == '__main__':
    banco = Banco()
    banco.executar()