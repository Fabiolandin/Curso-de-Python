"""
Dicionarios

Em algumas linguages dicionarios são iguais a mapas

Dicionarios são representados por chaves {}.
"""
#Forma 1 - a mais comum
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguay'}
print(paises)
print(type(paises))

#Forma 2 - Menos comum
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')
print(paises)
print(type(paises))


#Acessando elementos

#Forma 1 - Acessando via chave
print(paises['br'])
print(paises['eua'])

#Forma 2 - Acessando via get - recomendada
print(paises.get('eua'))
print(paises.get('py'))

#Podemos utilizar qualquer tipo de dados
localidades = {
    (35.668, 39.6917): 'Escritório em Tókyo',
    (42.998, 74.4124): 'Escritório em São Paulo',
    (95.124, 23.2352): 'Escritório em New York',
}

print(localidades)

#Adicionar elementos em um dicionario
receita = {'jan': 100, 'fev':120, 'mar': 300}

print(type(receita))
print(receita)

#Forma 1 - Mais comum
receita['abr'] = 350
print(receita)

#Forma 2 - Menos comum
novidade = {'mai': 500}
receita.update(novidade)
print(receita)

