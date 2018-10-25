from generation import genAndSave, load, GenerationGraf
import time
# graph={ 0:[1,3,4], 1:[0,2,4], 2:[1,6], 3:[0,4,6], 4:[0,1,3,5], 5:[4], 6:[2,3] }
#weight={(0,1):2}

def bfs(graph, start, weight = None, end = None):
     print(end)
     path = []
     queue = [start]
     newPath = []
     visited = []
     for i in range(N*N-1):
        visited.append(False)
     op = 0
     start = time.time()
     while queue:
         # print(queue)
         op += 1
         vertex = queue.pop(0)
         if vertex == end or end in graph[vertex]:
             path.append(vertex)
             path.append(end)
             newPath = path[:]
             break
         if visited[vertex] == True:
             continue
         if vertex not in path:
             path.append(vertex)
             visited[vertex] = True
         for X in graph[vertex]:
             op += 1
             if visited[X] == False and X not in queue:
                 queue = [X] + queue
     finish = time.time() - start
     print("Операций", op)
     print(finish)
     # print("Обход графа = ", path)
     newPath = newPath[::-1]
     # print("Обход до финиша = ", newPath)
     tmp = []
     for i in newPath:
         if end in graph[i]:
             tmp.append((end, i))
             end = i
     # print('Путь = ', tmp)
     print(len(tmp))
     return newPath


# не ускоряется
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))

if __name__ == "__main__":
    N = 1000
    # genAndSave(N)
    graph, weight = load()
    #print(graph)
    print("СЧИТАНО")
    x = 1
    y = 500
    graph.update({x: graph[x] + [y]})
    graph.update({y: graph[y] + [x]})
    weight[(x, y)] = 1491
    weight[(y, x)] = 1491
    result_path = bfs(graph, start=1, weight=weight, end=N*N)[::-1]
    # result_path = bfs_paths(graph,1, N*N)
    #print("Путь = ",result_path)
    sum = 0
    # print(weight)
    for a in range(len(result_path)-1):
        x = result_path[a]
        y = result_path[a+1]
        if weight.get((x, y)):
            sum += weight[(x, y)]
        elif weight.get((y, x)):
            sum += weight[(y, x)]
    print("Сумма пути = ", sum)
