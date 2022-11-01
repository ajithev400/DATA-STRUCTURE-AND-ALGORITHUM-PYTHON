from collections import defaultdict, deque

graph = defaultdict(list)

def addEdge(graph,u, v):
    graph[u].append(v)

def generate_edges(graph):
    edges = []

    for node in graph:
        for neighbour in graph[node]:
            edges.append((node,neighbour))
    return edges




def find_shortest_path(graph,start,end,path=[]):
    path = path+[start]
    if start == end:
        return path
    
    shortest = None
    for node in graph[start]:
        if node not in path:
            new_path = find_shortest_path(graph,node,end,path)

            if new_path:
                if not shortest or len(new_path)<len(shortest):
                    shortest = new_path
    
    return shortest

def find_shortest_path2(graph,start,end):
    dist = {start:[start]}
    q = deque(start)
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] =[dist[at],next]
                q.append(next)
    return dist.get(end)


addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'e','c')
print(generate_edges(graph))

# print(find_shortest_path(graph,'a','e'))
# print(find_shortest_path2(graph,'a','e'))