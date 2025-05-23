"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.


"""
import statistics

# Dados coletados de algum sensor
dados = [1.9, 2.8, 0.3, 4.1, -0.1, 5.3]

#Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(media)

#A filter recebe dois parametros sendo uma func e um iteravel
res = filter(lambda r: r >= media, dados)
print(list(res))

# Outro exemplo
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia']
print(paises)

res = filter(None, paises)
print(list(res))

print('\n \n \n')

# A diferenca entre map() e filter() é:
#map() -> recebe dois parametros, uma func e um iteravel e retorna um objeto mapeado
#Filter() -> recebe dois parametros, uma func e um iteravel e retorna um objeto filtrando apenas o elemento especificado

#Exemplo mais complexo
usuarios = [
    {"username": "Fabio", "tweets": ["Eu amo gatos", "Eu adoro pizzas"]},
    {"username": "Samuel", "tweets": []},
    {"username": "Leandro", "tweets": ["Eu amo gatos", "Eu adoro pizzas"]},
    {"username": "Renato", "tweets": ["Eu amo gatos", "Eu adoro pizzas"]},
    {"username": "Carlos", "tweets": []}
]

#Filtras os inativos
inativos = list(filter(lambda u: len(u["tweets"]) == 0, usuarios))
print(inativos)


#Combinar filter com map()
nomes = ['Vanessa', 'Ana', 'Maria', 'Ana Clara', 'Bianca', 'Flavia', 'Leticia', 'Sarah']

# Criar uma lista com nomes que tenha menos de 5 caracteres
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)