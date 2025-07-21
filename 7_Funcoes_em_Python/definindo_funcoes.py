"""
Definindo funções

- Funções são pequenos partes de códigos que realizam tarefas especificas.
- Pode ou não receber entradas de dados e retornar uma saída de dados.
- Util para utilizar procedimentos similares por repetidas vezes.

Em python a forma geral de definir uma funcção é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:

nome_da_funcao -> Sempre, com letras minusculas, e se for nome composto com _
parametros_de_entrada são opcionais
"""

#Definindo a primeira fução

def diz_oi():
    print('Oi!')

"""
Obs: veja que dentro da função podemos utilizar outras funções!!!
Veja que nossa função só executa uma tarefa, que é dizer OI!
Veja que essa função não recebe nenhum parametro de entrada
Veja que essa função não retorna nada!
"""

#Utilizando funções

#Chamada de execução
diz_oi()

#NUNCA ESQUEÇA DE UTILIZAR O PARENTESES AO UTILIZAR UMA FUNÇÃO

#Exemplo 2

def cantar_parabens():
    print('Parabens pra voce!')
    print('Nesta data querida!')
    print('Muitas felicidades!')
    print('Muitos anos de vida!')

cantar_parabens()

#Pouco comum mas é possivel
canta = cantar_parabens

canta()