from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_flot_str_moeda


produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    pass

def menu() -> None:
    print('==============================')
    print('======== Bem-vindo(a) ========')
    print('======= Landinhos Shop =======')
    print('==============================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Comprar produtos')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Saindo do sistema...')
        sleep(2)
        exit()
    else:
        print('Opção invalida!')
        sleep(1)
        menu()

def cadastrar_produto() -> None:
    print('Cadastro de Produto')
    print('===================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)
    produtos.append(produto)

    print(f'O produto {nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()

def listar_produto() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos')
        print('====================')
        for produto in produtos:
            print(f'Código: {produto.codigo}')
            print(f'Nome: {produto.nome}')
            print(f'Preço: {produto.preco}')
            print('=====================')
            sleep(2)
    else:
        print('Nenhum produto foi cadastrado.')
        sleep(1)
        menu()
    menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar o carrinho: ')
        print('============================================================')
        print('=================== Produtos Disponíveis ===================')
        for produto in produtos:
            print(produto)
            print('============================================================')
            sleep(2)
        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'Quantidade de {produto.nome} no carrinho: {quant + 1} unidades')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                    if not tem_no_carrinho:
                        prod = {produto: 1}
                        carrinho.append(prod)
                        print(f'O produto {produto.nome} foi adicionado ao carrinho!')
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho!')
                sleep(2)
                menu()

        else:
            print(f'O produto com código {codigo} não foi encontrado.')
            sleep(2)
            menu()
    else:
        print('Ainda não existe produto cadastrado!')
    sleep(2)
    menu()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('=======================')
                sleep(2)
    else:
        print('Nenhum produto foi colocado no carrinho.')
    sleep(2)
    menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos no Carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('=======================')
                sleep(2)
                print(f'Sua fatura é: {formata_flot_str_moeda(valor_total)}')
                print('Volte sempre!')
                carrinho.clear()
                sleep(5)
    else:
        print('Nenhum produto foi colocado no carrinho.')
        sleep(2)
        menu()

def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == '__main__':
    main()
    menu()