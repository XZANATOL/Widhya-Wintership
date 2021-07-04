#include <iostream>

using namespace std;

int distance_sum(int arr[], int n){

    // sort array using bubble sort (can be more efficient if used insertion sort)
    for(int i=0; i<n; i++){
        for(int j=i+1; j<n; j++){
            if(arr[j] < arr[i]){
                int temp= arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
            }
        }
    }

    // Manhattan sum for each axis
    int res=0,sum=0;
    for(int i=0; i<n; i++){
        res+= arr[i]*i -sum;
        sum+= arr[i];
    }

    // return the result
    return res;
}

int totaldistancesum(int x[],int y[],int n){
    return distance_sum(x,n) + distance_sum(y,n);
}

int main()
{
    int n;
    cout << "Enter number of points > ";
    cin >> n;

    cout << endl;

    int x[n];
    for(int i=0; i<n; i++){
        cout << "Enter X" << i << " value > ";
        cin >> x[i];
    }

    cout << endl;

    int y[n];
    for(int i=0; i<n; i++){
        cout << "Enter Y" << i << " value > ";
        cin >> y[i];
    }

    cout << endl;

    cout << "Sum of Manhattan distance between all pairs of coordinates: " << totaldistancesum(x,y,n) << endl;


    return 0;
}
