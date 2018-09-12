# -1 - inf
D = [[0, 1, 2, 1],
    [2, 0, 7, -1],
    [6, 5, 0, 2],
    [1, -1, 4, 0]]

def Floyd_Warshall(D):
    for k in range(len(D)):
        for i in range(len(D)):
            for j in range(len(D)):
                if D[i][j] > 0 and D[i][k] > 0 and D[k][j] > 0:
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j])
                elif D[i][j] < 0 and D[i][k] > 0 and D[k][j] > 0:
                    D[i][j] = D[i][k] + D[k][j]

    return D
print(Floyd_Warshall(D))
