"""
Manipulando Data e Hora

Python tem um módulo Built-in para se trabalhar com data e hora chamado datetime
"""
import datetime

#print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MINYEAR)

print(datetime.datetime.now())

#replace() para fazer ajustes na data/hora
inicio = datetime.datetime.now()
print(inicio)

#Alterando o horário para 16 horas, 0 minuto, 0 segundo, 0 microsegundo
inicio = inicio.replace(year=2023, hour=16, minute=0, second=0, microsecond=0)
print(inicio)

#Criando uma hora/evento
evento = datetime.datetime(2019, 1, 1, 0)
print(evento)

nascimento = input("Informe sua data de nascimento (dd/mm/yyyy): ")
nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(type(nascimento))

# Acessa individual dos elementos de data e hora

print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)

