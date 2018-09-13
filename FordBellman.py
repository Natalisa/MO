graph={ 0:[1,3,4], 1:[0,2,4], 2:[1,6], 3:[0,4,6], 4:[0,1,3,5], 5:[4], 6:[2,3] }
weight={(0,1):2,(0,4):4,(0,3):5,(1,4):3,(1,2):1,(4,3):4,(4,5):2,(2,6):2,(3,6):1,
        (1,0):2,(4,0):4,(3,0):5,(4,1):3,(2,1):1,(3,4):4,(5,4):2,(6,2):2,(6,3):1}

def FordBelman(graph,weight,start,end=None):
    INF = 10 ** 9
    n = len(graph)
    dist = [INF] * n
    dist[start] = 0
    Stop = False
    k = 1
    Prev = [None] * n
    while k < n and not Stop:
        k += 1
        Stop = True
        for j, i in weight.keys():
            if dist[j] + weight[j, i] < dist[i]:
                dist[i] = dist[j] + weight[j, i]
                Stop = False
                Prev[i] = j
    if end is None:
        return (dist)
    path = []
    while end is not None:
        path.append(end)
        end = Prev[end]
    path = path[::-1]
    return (path)
print("Расстояния от стартовой вершины до остальных:\n",FordBelman(graph,weight,1))
print("Путь от стартовой вершины до конечной:\n",FordBelman(graph,weight,1,3))
