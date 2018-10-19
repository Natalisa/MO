import generation as g
import pickle
import time
from generation import genAndSave, load, GenerationGraf
N = 100

#graph={ 0:[1,3,4], 1:[0,2,4], 2:[1,6], 3:[0,4,6], 4:[0,1,3,5], 5:[4], 6:[2,3] }

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited)
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in (set(graph[vertex] )- set(path)):
            if next == goal:
                return path + [next]
            else:
                stack.append((next, path + [next]))


if __name__ == "__main__":
    genAndSave(N,N)
    graph, weight = load()
    result_path = dfs_paths(graph,1,N*N)
    sum = 0
    for a in range(len(result_path)-1):
        x = result_path[a]
        y = result_path[a+1]
        if weight.get((x, y)):
            sum += weight[(x, y)]
        elif weight.get((y, x)):
            sum += weight[(y, x)]
    print("Сумма пути = ", sum)
