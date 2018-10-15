import generation as g
import pickle
import time
#graph={ 0:[1,3,4], 1:[0,2,4], 2:[1,6], 3:[0,4,6], 4:[0,1,3,5], 5:[4], 6:[2,3] }
#weight={(0,1):2}

def genAndSave():
    graph, weight = g.GenerationGraf(100, 100)
    with open('graph.pickle', 'wb') as f:
        pickle.dump(graph, f)
    with open('weight.pickle', 'wb') as f:
        pickle.dump(weight, f)

def load():
    with open('graph.pickle', 'rb') as f:
        graph = pickle.load(f)
    with open('weight.pickle', 'rb') as f:
        weight = pickle.load(f)
    return graph, weight

# print (graph, weight, sep='\n')
def bfs(graph, start, weight = None, end = None):
     path = []
     queue = [start]
     newPath = []
     visited = [start]

     start = time.time()
     while queue:
         vertex = queue.pop(0)
         if vertex not in path:
             path.append(vertex)
         if vertex == end:
             newPath = path[:]
         for X in graph[vertex]:
             if X not in visited:
                 queue.append(X)
                 visited.append(X)
     finish = time.time() - start
     print(finish)
     print("Обход графа = ", path)
     newPath = newPath[::-1]
     print("Обход до финиша = ", newPath)
     tmp = []
     for i in newPath:
         if end in graph[i]:
             tmp.append((end, i))
             end = i
     print('Путь = ', tmp)
     print(len(tmp))
     if end is None:
         return path
     return tmp


if __name__ == "__main__":
    genAndSave()
    graph, weight = load()
    result_path = bfs(graph, start=1, weight=weight, end=100 * 100)
    sum = 0
    for a,b in result_path:
        sum += weight[(b,a)]
    print("Сумма пути = ", sum)
