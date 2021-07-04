#include <iostream>
#include <bits/stdc++.h>

using namespace std;

//Global Variables that will be used in the algorithm
int V,E;

//Functions declares
void bellmanFord(int G[][3], int S);
void shortest_path(int distance[]);

int main()
{
    cout << "Enter number of vertices > ";
    cin >> V;

    cout << "\nEnter number of edges > ";
    cin >> E;

    //Fill graph edges
    int G[E][3];
    for(int i=0; i<E; i++){
        cout << "Enter Edge [x,y,v] > ";
        cin >> G[i][0] >> G[i][1] >> G[i][2];
    }

    int S;
    cout << "Enter Source point index > ";
    cin >> S;

    bellmanFord(G, S);

    return 0;
}

void bellmanFord(int G[][3], int S){
    int distance[V];
    for(int i=0; i<V; i++){ //Filling the whole array with inf
        distance[i] = INT_MAX;
    }
    distance[S] = 0;

    for(int i=0; i<(V-1); i++){ //For each vertex in the graph
        for(int j=0; j<E; j++){ //For each edge in the graph
            int x = G[j][0];
            int y = G[j][1];
            int z = G[j][2];
            int temp= distance[x] + z;
            if(temp < distance[y]){
                distance[y] = temp;
            }
        }
    }

    for(int i=0; i<E; i++){ //To check for negative cycles
        int x = G[i][0];
        int y = G[i][1];
        int z = G[i][2];
        if((distance[x] + z) < distance[y]){
            cout << endl << "Negative cycle exists" << endl;
            break;
        }
    }


    shortest_path(distance);

    return;
}

void shortest_path(int distance[]){
    // sort array using bubble sort (can be more efficient if used insertion sort)
    for(int i=0; i<V; i++){
        for(int j=i+1; j<V; j++){
            if(distance[j] < distance[i]){
                int temp= distance[j];
                distance[j] = distance[i];
                distance[i] = temp;
            }
        }
    }

    cout << endl << "Final shortest path stored in 'distance' is: " << distance[0];

    return;
}
