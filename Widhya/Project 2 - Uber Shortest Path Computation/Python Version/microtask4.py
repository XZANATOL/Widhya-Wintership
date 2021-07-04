import heapq as h

def Dijsktra(graph, start):
    # Set all vertices distances = infinity except for the source vertex = 0
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0

    # Push the source vertex to a min-priority queue in the form (distance, vertex)
    pq =[(0, start)]

    while pq:
        # pop the vertix with the minimum distance (first pooped vertex = source)
        distance, vertex = h.heappop(pq)

        # if popped vertex is visited before, just continue without using it
        if distance > distances[vertex]:
            continue

        # update the distances ofthe connected vertices to the popped vertex
        for v, w in graph[vertex].items():
            temp = distance+w # (current vertex distance + edge weight)
            if temp < distances[v]: # if temp < next vertex distance
                distances[v] = temp
                h.heappush(pq, (temp, v))

    return distances



if __name__ == '__main__':
    pass
    """
    #for testing
    example_graph = {
        'U': {'V': 2, 'W': 5, 'X': 1},
        'V': {'U': 2, 'X': 2, 'W': 3},
        'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
        'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
        'Y': {'X': 1, 'W': 1, 'Z': 1},
        'Z': {'W': 5, 'Y': 1},
    }
    print(Dijsktra(example_graph, 'X'))"""
