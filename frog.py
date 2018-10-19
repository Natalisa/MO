path = [0, 1, 2, 3, 6, 8, 10, 11, 13, 15, 18, 20]
lvl = []
INF = 10**2
# 0-1-3-6-10-15-20
# < на +1 от предыдущ
# 6
def printTable(prth, lvl):
    print("P",end='\t')
    for i in range(0,len(lvl)):
        print(i, end='\t')
    print()
    for num, row in enumerate(lvl):
        print(path[num], end='\t')
        for tmp in row:
            if tmp is INF:
                print("-",end='\t')
            else:
                print(tmp, end='\t')
        print()

if __name__ == "__main__":
    L = len(path)
    for j in range(L):
        tmp = []
        for i in range(L):
            tmp.append(INF)
        lvl.append(tmp)

    lvl[0][0] = 0

    ind = 0

    for i in range(1, L):
        for j in range(len(lvl)):
            if path[i] - j in path and path[i] - j < path[i]:
                cell = lvl[path.index(path[i] - j)]
                if path[i]-j in path and j + 1 < len(lvl):
                    minimum = min(cell[j-1], cell[j], cell[j+1])
                elif path[i]-j in path:
                    minimum = min(cell[j-1], cell[j])
                if minimum != INF:
                    lvl[i][j] = minimum + 1

    printTable(path, lvl)

    minimum = min(lvl[-1])
    ind = lvl[-1].index(min(lvl[-1]))
    recoverPath = []
    recoverPath.append(path[-1])
    #print("min",minimum,"id", ind, recoverPath)
    while minimum != 0:
        recoverPath.append(path[ path.index(path[path.index(recoverPath[-1])] - ind) ])
        minimum = min(lvl[ path.index(recoverPath[-1] ) ])
        ind = lvl[path.index(recoverPath[-1] )].index(min(lvl[path.index(recoverPath[-1] )]))
        #print("min",minimum,"id", ind, recoverPath)
        if minimum == INF:
            print("Решение не найдено")
            exit(-1)

    print("Оптимальный путь =", recoverPath[::-1])
