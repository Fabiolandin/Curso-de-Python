"""
Escrevendo em arquivos CSV

reader() (leitor), writer() (escritor)

writerow() -> Escreve uma linha no arquivo CSV

#writer gera um objeto para que possamos escrever um arquivo.csv. Utilizamos o mét0do
#writerow() para escrever cada linha. Este mét0do recebe uma lista

from csv import writer, DictWriter

with open('filmes.csv', 'w', encoding='utf-8', newline='') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Digite o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o Gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])
"""
#writer gera um objeto para que possamos escrever um arquivo.csv. Utilizamos o mét0do
#writerow() para escrever cada linha. Este mét0do recebe uma lista

#Se quiser adicionar em vez de sobrescrever é só trocar o w por A

from csv import writer, DictWriter

with open('filmes.csv', 'w', encoding='utf-8', newline='') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Digite o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o Gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])

from csv import writer, DictWriter

# DictWriter
with open('filmes2.csv', 'w', encoding='utf-8', newline='') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Digite o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o Gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow({"Título": filme, 'Gênero': genero, 'Duração': duracao})
