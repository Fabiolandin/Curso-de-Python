def comer(comida, saudavel):
    if saudavel:
        final = 'quero manter a forma.'
    else:
        final = 'só se vive uma vez.'

    return f'Estou comendo {comida} porque {final}'

def dormir(horas):
    if horas > 8:
        return f'Dormi pra caramba filho!.'
    else:
        return f'Continuo cansado após dormir {horas} horas.'


def engracada(pessoa):
    comediantes = ['Jim Carrey', 'Bozo', 'Renato Albani', 'Victor Sarro']
    if pessoa in comediantes:
        return True
    else:
        return False