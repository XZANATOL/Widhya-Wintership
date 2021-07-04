#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    float x1,x2,y1,y2,D;

    cout << "Enter X1 and Y1 coordinates [x1 y1] > ";
    cin >> x1 >> y1;

    cout << "Enter X2 and Y2 coordinates [x2 y2] > ";
    cin >> x2 >> y2;

    D = pow( (pow((x2-x1), 2) + pow((y2-y1), 2) ),0.5);
    cout << "Distance between both points is: " << D << endl;

    return 0;
}
