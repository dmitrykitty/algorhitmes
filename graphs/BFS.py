from collections import deque

#BFS
def BFS(graph, source):
    Q = deque([source])
    parent = {}
    discovered = set()
    while Q:
        v = Q.popleft()
        for neighbour in graph[v]:
            if neighbour not in discovered:
                discovered.add(neighbour)
                parent[neighbour] = v
                Q.append(neighbour)
    return parent


#Print path
def print_path(source, target, parent):
    if source == target:
        print(source, end=' ')

    elif target not in parent:
        print("Path does not exist")

    else:
        print_path(source, parent[target], parent)
        print(target, end=' ')



parent_map = {'B': 'A', 'C': 'A', 'D': 'B', 'I': 'B', 'F': 'C', 'G':'C', 'E': 'D', 'H': 'I'}
# source = 'A'
# target = 'F'

print_path('A', 'H', parent_map)