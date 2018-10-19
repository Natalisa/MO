import generation as g
import pickle
import time
from bfs import genAndSave, load
N = 3

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
    genAndSave()
    graph, weight = load()
    print(graph)
    # result_path = bfs2(graph, start=1, weight=weight, end=N*N)
    result_path = dfs_paths(graph,1,N*N)
    print(result_path)
    sum = 0
    # for a,b in result_path:
    #     sum += weight[(b,a)]
    # print("Сумма пути = ", sum)
