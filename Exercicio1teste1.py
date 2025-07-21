def getMinimumIncrement(arr):
    n = len(arr)
    candidatos_x = []  # Armazenará os valores de x necessários

    # Passo 1: Identificar onde o array não é não-decrescente
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            diferenca = arr[i - 1] - arr[i]
            # Tentamos primeiro incrementar o elemento atual (arr[i])
            if i == 1 or (i > 1 and arr[i - 2] <= arr[i] + diferenca):
                candidatos_x.append(diferenca)
            elif i < n - 1 and arr[i + 1] >= arr[i - 1]:
                candidatos_x.append(diferenca)
            else:
                return -1

    if not candidatos_x:
        return 0

    x = max(candidatos_x)

    copia_arr = arr.copy()  # Criamos uma cópia para testar

    for i in range(n):
        if i > 0 and copia_arr[i] < copia_arr[i - 1]:
            if i < n - 1 and copia_arr[i + 1] >= copia_arr[i - 1]:
                copia_arr[i] += x
            else:
                return -1

    for i in range(1, n):
        if copia_arr[i] < copia_arr[i - 1]:
            return -1

    return x