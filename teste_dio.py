# Entrada simulada
pacientes_entrada = [
    "Carlos, 40, normal",
    "Ana, 70, normal",
    "Bruno, 30, urgente"
]

# Lista que armazenará os dados parseados
pacientes = []

for linha in pacientes_entrada:
    nome, idade, status = linha.strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TOD0: Ordene por prioridade: urgente > idosos > demais:


# TOD0: Exiba a ordem de atendimento com título e vírgulas:

