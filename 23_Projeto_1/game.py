from models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe a dificuldade do jogo [1, 2, 3 ou 4] '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinta operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())
    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Voce tem {pontos} pontos')

    continuar: int = int(input('Deseja continuar no jogo? [1 - Sim/0 - Não] '))
    if continuar:
        jogar(pontos)
    else:
        print(f'Voce finalizou com {pontos} pontos')
        print('Até a próxima')

if __name__ == '__main__':
    main()