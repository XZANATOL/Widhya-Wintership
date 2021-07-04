def bellmanFord(G, S):
    global V
    distance = [float("inf")] * V
    distance[S] = 0

    for _ in range(V-1):  # for each vertex in the graph
        for x, y, z in G:
            temp = distance[x] + z
            if temp < distance[y]:
                distance[y] = temp

    for x, y, z in G:  # to check for negative cycles
        if distance[x] + z < distance[y]:
            print("Negative cycle exists")

    shortest_path(distance) # pass distance list to the print function


def add_edge(data):
    global G
    G.append(data)


def shortest_path(distance):  # Print final shortest path
    min = sorted(distance)[0]
    print("Final shortest path stored in 'distance' is: {}".format(min))


if __name__ == '__main__':
    V = int(input("Enter number of vertices > "))
    E = int(input("\nEnter number of edges > "))
    G = []
    for i in range(E):
        x, y, v = map(int, input("Enter Edge [x,y,v] > ").split(" "))
        add_edge([x, y, v])

    S = int(input("Enter source point index > "))

    bellmanFord(G, S)
