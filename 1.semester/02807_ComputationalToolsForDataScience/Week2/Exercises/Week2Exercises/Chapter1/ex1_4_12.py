x = [[1, 2],
     [3, 4],
     [5, 6]]

def transposeMatrix(x):
    xTranspose = [[0 for a in range(len(x))] for b in range(len(x[1]))]
    for i in range(0, len(x)):
        for j in range(0, len(x[i])):
            xTranspose[j][i] = x[i][j]
    return xTranspose

print(transposeMatrix(x))