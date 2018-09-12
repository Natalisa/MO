graph={ 0:[1,3,4], 1:[0,2,4], 2:[1,6], 3:[0,4,6], 4:[0,1,3,5], 5:[4], 6:[2,3] }

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited)
    return visited
print(dfs(graph,1))
