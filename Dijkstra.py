graph={ 0:[1,3,4], 1:[0,2,4], 2:[1,6], 3:[0,4,6], 4:[0,1,3,5], 5:[4], 6:[2,3] }
weight={(0,1):2,(0,4):4,(0,3):5,(1,4):3,(1,2):1,(4,3):4,(4,5):2,(2,6):2,(3,6):1,
        (1,0):2,(4,0):4,(3,0):5,(4,1):3,(2,1):1,(3,4):4,(5,4):2,(6,2):2,(6,3):1}

def Dijkstra(graph,weight,start,end=None):
    INF = 10 ** 10
    n = len(graph)
    dist = [INF] * n
    dist[start] = 0
    prev = [None] * n
    used = [False] * n
    min_dist = 0
    min_vertex = start
    while min_dist < INF:
        i = min_vertex
        used[i] = True
        for j in graph[i]:
            if dist[i] + weight[i, j] < dist[j]:
                dist[j] = dist[i] + weight[i, j]
                prev[j] = i
        min_dist = INF
        for i in range(n):
            if not used[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_vertex = i
    if end is None:
        return (dist)
    path = []
    while end is not None:
        path.append(end)
        end = prev[end]
    path = path[::-1]
    return (path)

print("Расстояния от стартовой вершины до остальных:\n",Dijkstra(graph,weight,1))
print("Путь от стартовой вершины до конечной:\n",Dijkstra(graph,weight,1,3))
