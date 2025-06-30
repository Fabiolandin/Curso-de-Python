"""
Métodos de Data Hora


"""
import datetime
#Com now podemos especificar um timezona "fuzo horario", com today não
agora = datetime.datetime.now() # agora
hoje = datetime.datetime.today() #hoje
print(agora)
print(hoje)

# Mudanças ocorrendo a meia-noite combine()
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)

#Encontrar o dia da semana, weekday()
# Os dias da semana do mét0do weekday começa em 0 sendo 0 segunda-feira
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao.weekday())

aniversario = str('13/09/2002')

aniversario = aniversario.split('/')

aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Voce nasceu em uma segunda-feira')
elif aniversario.weekday() == 1:
    print('Voce nasceu em uma terca-feira')
elif aniversario.weekday() == 2:
    print('Voce nasceu em uma quarta-feira')
elif aniversario.weekday() == 3:
    print('Voce nasceu em uma quinta-feira')
elif aniversario.weekday() == 4:
    print('Voce nasceu em uma sexta-feira')
elif aniversario.weekday() == 5:
    print('Voce nasceu em um sábado')
elif aniversario.weekday() == 6:
    print('Voce nasceu em um Domingo')

"""
#Formatando as horas pra pt-br
hoje = datetime.datetime.today()
print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%Y')
print(hoje_formatado)
"""

#Exemplo 2 de Formatando as horas pra pt-br
def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'

hoje = datetime.datetime.today()

print(formata_data(hoje))


#Exemplo3
nascimento = str('13/09/2002')
nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
print(nascimento)


