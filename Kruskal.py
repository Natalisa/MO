graph={ 0:[1,3,4], 1:[0,2,4], 2:[1,6], 3:[0,4,6], 4:[0,1,3,5], 5:[4], 6:[2,3] }
weight={(0,1):2,(0,4):4,(0,3):5,(1,4):3,(1,2):1,(4,3):4,(4,5):2,(2,6):2,(3,6):1,
        (1,0):2,(4,0):4,(3,0):5,(4,1):3,(2,1):1,(3,4):4,(5,4):2,(6,2):2,(6,3):1}
#[weight, start, end]
Edges = [[2,1,0],[4,0,4],[5,0,3],[3,1,4],[1,1,2],[4,3,4],[2,4,5],[2,2,6],[1,6,3]]

def Kruskal(graph,Edges):
    Edges.sort()
    N = len(graph)
    Comp = [i for i in range(N)]
    Ans = 0
    Ostov = []
    for weight, start, end in Edges:
        if Comp[start] != Comp[end]:
            Ans += weight
            a = Comp[start]
            b = Comp[end]
            Ostov.append([start,end])
            for i in range(N):
                if Comp[i] == b:
                    Comp[i] = a
    return (Ans, Ostov)
print("Вес, остов ",Kruskal(graph,Edges))
