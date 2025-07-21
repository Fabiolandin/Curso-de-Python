"""
Try / Except / Else / Finally

Dica de quando e onde tratar o código:

TODA ENTRADA DEVE SER TRATADA!

try:
    num = int(input('Informe um numero'))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Voce digitou {num}')

#Finally - sempre sera executado ao final.
try:
    num = int(input('Informe um numero'))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Voce digitou {num}')
finally:
    print('Volte sempre!!')

#Geralmente o finally é utilizado para fechar ou desalocar recursos.
"""
#Exemplo correto
def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return ('Valor incorreto')
    except ZeroDivisionError:
        return ('Não pode dividir por 0')

num1 = input('Informe um numero: ')
num2 = input('Informe um numero: ')

print(dividir(num1, num2))
