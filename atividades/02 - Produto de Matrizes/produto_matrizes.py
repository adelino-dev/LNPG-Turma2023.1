def multiplicarMatrizes(a, b):
    matriz = []
    linhasA = len(a)
    colunasA = len(a[0])
    colunasB = len(b[0])

    for iA in range(linhasA):
        linha = []
        for jB in range(colunasB):
            n = 0
            for jA in range(colunasA):
                n += a[iA][jA] * b[jA][jB]
            linha.append(n)
        matriz.append(linha)

    return matriz

a = [[1, 2, 3], 
     [4, 5, 6]]

b = [[3, 6, 9],
     [4, 7, 10],
     [5, 8, 11]]

print(multiplicarMatrizes(a,b))