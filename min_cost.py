Stocks = [30, 40, 20]
Needs = [20, 30, 30, 10]
ResultMatrix = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
N = 3
M = 4
Matrix = [[2, 3, 2, 4],
          [3, 2, 5, 1],
          [4, 3, 2, 6]]

def minimimInMatrix():
    min = 9999
    minI = 0
    minJ = 0
    for i, row in enumerate(Matrix):
        for j, el in enumerate(row):
            if el < min:
                minI = i
                minJ = j
                min = el
    return (min, minI, minJ)


if __name__ == "__main__":
    currentStock = 0
    currentNeed = 0
    while sum(Needs) != 0:
        (minimum, currentStock, currentNeed) = minimimInMatrix()
        print(ResultMatrix)
        if Stocks[currentStock] >= Needs[currentNeed]:
            ResultMatrix[currentStock][currentNeed] = Needs[currentNeed] # * Matrix[currentStock][currentNeed]
            Stocks[currentStock] -= Needs[currentNeed]
            Needs[currentNeed] = 0
        elif Stocks[currentStock] < Needs[currentNeed]:
            Needs[currentNeed] -= Stocks[currentStock]
            ResultMatrix[currentStock][currentNeed] = Stocks[currentStock] # * Matrix[currentStock][currentNeed]
            Stocks[currentStock] = 0
        Matrix[currentStock][currentNeed] = 10 ** 6
        print(ResultMatrix, '\n')
    print(ResultMatrix)
