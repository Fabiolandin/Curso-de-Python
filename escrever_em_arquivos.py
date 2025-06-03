"""
Escrevendo em arquivos

#Obs: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

#Obs: ao abrir um arquivo para escrita um arquivo é criado no sistema operacional

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir ser criado
caso ele ja exista o anterior sera apagado e o novo sera criado "reescrito".
"""
#Forma Pythonica
#Exemplo de escrita - modo 'w' -write (escrita)
with open("arquivo.txt", 'w') as arquivo:
    arquivo.write("Olá, Mundo!\n")
    arquivo.write("Eu me chamo FABIO LANDIN!\n")

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Insira o fruta ou digite sair: ')
        if fruta == 'sair':
            arquivo.write(fruta + '\n')
        else:
            break

