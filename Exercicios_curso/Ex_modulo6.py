"""
1. Crie um programa que.
Crie/abra um arquivo texto de nome “arq.txt”.
Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere “0”.
Feche o arquivo.
Abra, leia o arquivo e escreva na tela todos os caracteres armazenados.
"""
with open('arq.txt', 'w') as arquivo:
    while True:
        caractere: str = input('Digite uma caractere ou 0 para sair: ')

        if caractere != '0':
            arquivo.write(f'{caractere} \n')
        else:
            break

with open('arq.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:
    print(linha)


"""
2. Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas letras são
vogais e quantas são consoantes.
"""
vogais: int = 0
consoantes: int = 0
arq: str = input('Digite o nome de um arquivo texto: ')

with open(arq, 'r') as arq:
    linhas = arq.readlines()

for linha in linhas:
    if linha.replace('\n', '').lower() in ['a', 'e', 'i', 'o', 'u']:
        vogais = vogais + 1
    else:
        consoantes = consoantes + 1

if vogais > 0:
    print(f'Existe {vogais} vogais no arquivo')
else:
    print('Não existe vogais no arquivo')

if consoantes > 0:
    print(f'Existe {consoantes} vogais no arquivo')
else:
    print('Não existe consoantes no arquivo')


"""
3. Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas linhas este
arquivo possui.
"""
arquivo: str = input('Digite o nome de um arquivo texto: ')

with open(arquivo, 'r') as arq:
    linhas = arq.readlines()

print(f'Existe {linhas} linhas no arquivo')