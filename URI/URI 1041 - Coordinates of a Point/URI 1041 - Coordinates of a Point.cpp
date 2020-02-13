#include<bits/stdc++.h>
using namespace std;

int main(){

    double zero = 0;
    double x, y;
    cin >> x >> y;

    if (x == zero && y == zero)
        cout << "Origem" << endl;
    else if (x == zero)
        cout << "Eixo Y" <<endl;
    else if (y == zero)
        cout << "Eixo X" <<endl;
    else if (x > zero && y > zero)
        cout << "Q1" <<endl;
    else if (x < zero && y > zero)
        cout << "Q2" <<endl;
    else if (x < zero && y < zero)
        cout << "Q3" <<endl;
    else
        cout << "Q4" <<endl;

    return 0;
}