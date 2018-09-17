graph={ 0:[1,3,4], 1:[0,2,4], 2:[1,6], 3:[0,4,6], 4:[0,1,3,5], 5:[4], 6:[2,3] }
weight={(0,1):2}
def GenerationGraf(n,m=None):
    if m is None:
        m = n
    graph = {}
    weight = {}
    count = 1
    for i in range(n*(m-1)):
        weight[(count,count+n)] = 1
        if count%n != 0:
            weight[(count,count+1)] = 1
        count = count + 1
    for i in range(n-1):
        weight[(count,count+1)] = 1
        count = count + 1
    for i in weight.keys():
        key,val = i
        if graph.get(key) is None:
            graph[key] = [val]
        else:
            tmp = graph.get(key)
            tmp.append(val)
            graph[key] = tmp
        if graph.get(val) is None:
            graph[val] = [key]
        else:
            tmp = graph.get(val)
            tmp.append(key)
            graph[val] = tmp
    return(graph,weight)
