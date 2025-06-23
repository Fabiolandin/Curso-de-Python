"""
Forçando tipos de dados com decoradores


"""

def forca_tipo(*tipos):
    def decorator(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*args, **kwargs)
        return converte
    return decorator

@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)

repete_msg('Fabio', 5)

@forca_tipo(float, float)
def dividir(a, b):
    print(a / b)

dividir(1, 2)