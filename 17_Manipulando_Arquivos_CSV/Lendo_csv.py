"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores Separados por Vírgula

#Separador por virgula
1, 2, 3, 4, 5, 6, 7, 8, 9, 10
"Fabio", "Landin", "Junior"

#Separador por ponto e virgula
1; 2; 3; 4; 5; 6; 7; 8; 9; 10
"Fabio"; "Landin"; "Junior"

A linguagem python possui duas formas diferentes para ler dados em arquivos csv:
 - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
 - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;
"""
#Forma não ideal de trabalhar com CSV
with open('lutadores.csv', encoding='utf-8') as arquivo:
    dados = arquivo.read()
    #print(type(dados))
    dados = dados.split(',')[3:]
    print(dados)

# Reader
from csv import reader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) #Pula o cabeçalho
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu em {linha[1]} e mede {linha[2]} centimetros')

#DictReader
from csv import DictReader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']}")


#DictReader - com outro separador a não ser virgula
from csv import DictReader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',') #aqui se coloca se não for separado por ,
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']}")