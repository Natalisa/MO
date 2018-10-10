import generation as g

#graph={ 0:[1,3,4], 1:[0,2,4], 2:[1,6], 3:[0,4,6], 4:[0,1,3,5], 5:[4], 6:[2,3] }
graph,weight = g.GenerationGraf(2,10)
print (graph, weight, sep='\n')
def bfs(graph, start, weight = None, end = None):
     path = {}
     queue = [start]
     tmp = start
     while queue:
         vertex = queue.pop(0)
         if vertex not in path:
             path[vertex] = tmp
             queue.extend(graph[vertex])
         tmp = vertex
     if end is not None:
         tmp = end
         sum = 0
         while tmp is not start:
             sum += weight[(path[tmp],tmp)]
             print( weight[(path[tmp],tmp)],path[tmp],tmp)
     return path
print()
print (bfs(graph, 1, weight, 7))
