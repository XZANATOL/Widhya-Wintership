#include <iostream>
#include <bits/stdc++.h>

#define V 9

using namespace std;

//Global Variables that will be used in the algorithm

//Functions declares
void Dijkstra(int graph[V][V], int S);
void shortest_path(int distance[]);

int main()
{
    int graph[V][V] = { { 0, 4, 0, 0, 0, 0, 0, 8, 0 },
                        { 4, 0, 8, 0, 0, 0, 0, 11, 0 },
                        { 0, 8, 0, 7, 0, 4, 0, 0, 2 },
                        { 0, 0, 7, 0, 9, 14, 0, 0, 0 },
                        { 0, 0, 0, 9, 0, 10, 0, 0, 0 },
                        { 0, 0, 4, 14, 10, 0, 2, 0, 0 },
                        { 0, 0, 0, 0, 0, 2, 0, 1, 6 },
                        { 8, 11, 0, 0, 0, 0, 1, 0, 7 },
                        { 0, 0, 2, 0, 0, 0, 6, 7, 0 } };

    Dijkstra(graph, 0);

    return 0;
}

void Dijkstra(int graph[V][V], int S)
{
    int dist[V]; bool sptSet[V];

    for (int i = 0; i < V; i++){
        dist[i] = INT_MAX;
        sptSet[i] = false;
    }
    dist[S] = 0;

    for (int i=0; i<V-1; i++) {

        int mini = INT_MAX, min_index;
        for (int j=0; j<V; j++){
            if (sptSet[j] == false && dist[j] <= mini){
                mini = dist[j];
                min_index = j;
            }
        }

        sptSet[min_index] = true;

        for (int j=0; j<V; j++){

            if (!sptSet[j] && graph[min_index][j] && dist[min_index] != INT_MAX && dist[min_index] + graph[min_index][j] < dist[j]){
                dist[j] = dist[min_index] + graph[min_index][j];
            }
        }
    }

    shortest_path(dist);
}

void shortest_path(int distance[]){
    for(int i=0; i<V; i++){
        printf("%d      %d\n", i, distance[i]);
    }

}
