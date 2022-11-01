# from collections import defaultdict,deque

# graph = defaultdict(list)

# def add_edge(graph,u,v):
#     graph[u].append(v)

# def generate_edges(graph):
#     edges = []

#     for node in graph:
#         for neigbour in graph[node]:
#             edges.append((node,neigbour))
#     return edges

# def find_path(grap,start,end,path=[]):
#     path = path+[start]
#     if start == end:
#         return path

    
#     for node in graph[start]:
#         if node not in path:
#             new_path = find_path(graph,node,end,path)
#             if new_path:
#                 return new_path
    
#     return None



# add_edge(graph,'a','c')
# add_edge(graph,'b','c')
# add_edge(graph,'b','e')
# add_edge(graph,'c','d')  
# add_edge(graph,'c','e')
# add_edge(graph,'c','a')
# add_edge(graph,'c','b')
# add_edge(graph,'e','b')
# add_edge(graph,'d','c')
# add_edge(graph,'e','c')
# print(generate_edges(graph))

# print(find_path(graph,'a','e'))

from array import *

arr1 = array('i',[10,21,32,4,3])

for x in arr1:
    print(x)