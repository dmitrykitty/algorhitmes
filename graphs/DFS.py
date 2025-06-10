visited = set()


def DFS(graph, node):
    visited.add(node)
    print(node)
    for neighbor in graph[node]:
        if not neighbor in visited:
            DFS(graph, neighbor)


visited2 = set()


def DFS_matrix(graph, node):
    visited2.add(node)
    print(node)

    for j in range(len(graph)):
        if graph[node][j] != 0 and j not in visited2:
            DFS_matrix(graph, j)


graph = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1]
]

DFS_matrix(graph, 0)


def solve_campus_domination(campus_grid):
    n = len(campus_grid[0])
    visited = [[0] * n for i in range(n)]
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    def DFS(i, j, group):
        nonlocal is_on_border
        visited[i][j] = 1
        group.append((i, j))

        if i == 0 or j == 0 or i == n - 1 or j == n - 1:
            is_on_border = True

        for to_i, to_j in directions:
            new_i, new_j = i + to_i, j + to_j
            if 0 <= new_i < n and 0 <= new_j < n:
                if campus_grid[new_i][new_j] == 0 and not visited[new_i][new_j]:
                    DFS(new_i, new_j, group)

    for i in range(n):
        for j in range(n):
            if campus_grid[i][j] == 0 and not visited[i][j]:
                group_of_zeros = []
                is_on_border = False

                DFS(i, j, group_of_zeros)
                if not is_on_border:
                    for change_i, change_j in group_of_zeros:
                        campus_grid[change_i][change_j] = 1

    return campus_grid