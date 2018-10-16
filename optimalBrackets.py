matrixs1 = [[1,5],[5,20],[20,1]]
matrixs2 = [[5,10],[10,20],[20,35]]
matrixs3 = [[30,35],[35,15],[15,5],[5,10],[10,20],[20,25]]
INF = 10**9

matrix = matrixs3
p = []
count = len(matrix)
for i, j in matrix:
    if not(i in p):
        p.append(i)
    if not(j in p):
        p.append(j)

m = []
s = []
for i in range(count):
    m.append([])
    s.append([])
    for j in range(count):
        if i == j:
            m[i].append(0)
        else:
            m[i].append(INF)
        s[i].append(0)
print(p)
def mult(i, j):
    global s,p,m
    if m[i][j] == INF:
        for k in range(i, j):
            temp =  mult(i, k) + mult(k+1, j) + p[i-1]*p[k]*p[j]
            if temp < m[i][j]:
                m[i][j] = temp
                s[i][j] = k

    return m[i][j]

def printOp(i, j):
    global s
    if i == j:
        return "A"+str(i+1)
    return "(" + printOp(i, s[i][j])+"x" + printOp(s[i][j]+1, j) + ")"


mult(0, count-1)
print()
for i in m:
    print(i)
print()
for i in s:
    print(i)

if count == 1:
    print("(A1)")
else:
    print(printOp(0, count-1))
