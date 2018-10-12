Stocks = [30, 40, 20]
Needs = [20, 30, 30, 10]
ResultMatrix = [[0, 0, 0, 0],
				[0, 0, 0, 0],
				[0, 0, 0, 0]]

if __name__ == "__main__":
	currentStock = 0
	currentNeed = 0
	i = 0
	j = 0
	while True:
		if Stocks[currentStock] >= Needs[currentNeed]:
			ResultMatrix[i][j] = Needs[currentNeed]
			Stocks[currentStock] -= Needs[currentNeed]
			Needs[currentNeed] = 0
			currentNeed += 1
			j += 1
		elif Stocks[currentStock] < Needs[currentNeed]:
			ResultMatrix[i][j] = Stocks[currentStock]
			Needs[currentNeed] -= Stocks[currentStock]
			Stocks[currentStock] = 0
			currentStock += 1
			i += 1
		if i > 3 or j > 2:
			break
		print(i, j)
		print(ResultMatrix)
		print(Stocks)
		print(Needs)

	print(ResultMatrix)
