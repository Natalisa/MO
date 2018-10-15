path = [0, 1, 2, 3, 6, 8, 10, 11, 13, 15, 18, 20]
lvl = []

# 0-1-3-6-10-15-20
# < на +1 от предыдущ
# 6

if __name__ == "__main__":
    for j in range(len(path)):
        tmp = []
        for i in range(len(path)):
            tmp.append(10**2)
        lvl.append(tmp)

    lvl[0][0] = 0

    ind = 0
    # while ind < len(path):
    # print(lvl)
    # for i in range(len(path)):
    #     for j in range(6):
    #         if path[i] - j in path:
    #             minimum = min(lvl[i-path[i]][j], lvl[i-path[i]][j-1], lvl[i-path[i]][j+1])
    #             if minimum != 10**9:
    #                 print(path[i], j, minimum)
    #                 lvl[i][j] = minimum + 1
                # print(lvl[i][j])

    for i in range(1, len(path)):
        for j in range(len(lvl)):
            if path[i] - j in path and path[i] - j < path[i]:
                if path[i]-j in path and j + 1 < len(lvl):
                    minimum = min(lvl[path.index(path[i]-j)][j-1], lvl[path.index(path[i]-j)][j], lvl[path.index(path[i]-j)][j+1])
                elif path[i]-j in path:
                    minimum = min(lvl[path.index(path[i]-j)][j-1], lvl[path.index(path[i]-j)][j])
                if minimum != 10**2:
                    lvl[i][j] = minimum + 1
    for num, row in enumerate(lvl):
        print(path[num], row)
