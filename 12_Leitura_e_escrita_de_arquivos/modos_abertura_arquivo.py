"""
Modos de abertura de arquivo

r -> Abre para leitura de arquivo - padrão
w -> Abre para escrita - Sobrescreve caso o arquivo ja exista
x -> Abre para escrita somente se o arquivo n existir - caso o arquivo ja exista gera um FileExistsError
a -> Abre para escrita adicionando o conteúdo ao final do arquivo
+ -> abre para o modo de atualização: Leitura e escrita.

#Exemplo X
with open('university.txt', 'x') as arquivo:
    arquivo.write('Teste de conteúdo. \n')

#Exemplo A
with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe um fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
"""

