import heapq

def DIJKSTRY(graph, start):
    distances = {node: float('inf') for node in graph}
    parent = {}
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        current_distance, u = heapq.heappop(heap)
        if distances[u] > current_distance:
            for v, weight in graph[u]:
                distance_through_u = current_distance + weight
                if distance_through_u < distances[v]:
                    distances[v] = distance_through_u
                    parent[v] = u
                    heapq.heappush(heap, (distance_through_u, v))
    return distances, parent