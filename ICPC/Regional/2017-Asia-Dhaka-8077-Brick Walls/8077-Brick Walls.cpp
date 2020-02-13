#include <bits/stdc++.h>
using namespace std;

long long distance(long long s1, long long s2, long long d1, long long d2){
    if ((s1 && s2 && d1 && d2) == 0) return INT32_MAX;
    
    long long min_distance = abs ( (d1 - s1) * 2 );

    min_distance = (s1 + s2) % 2 ? min_distance + 1 : min_distance;

    long long distance = abs( d1-s1 ) + abs(d2-s2);

    return  max(min_distance, distance);

}

long long calc(long long s1, long long s2, long long d1, long long d2){

    if (abs( d1-s1 ) == abs(d2-s2)) return abs( d1-s1 ) * 2;

    if (s1 > d1)
        return calc(d1, d2, s1, s2);
    
    long long mainDist = distance(s1, s2, d1, d2);
    mainDist = min(mainDist, distance(s1, s2, d1, d2-1) + 1);
    mainDist = min(mainDist, distance(s1, s2, d1, d2+1) + 1);

    if ( (d1 + d2) % 2 == 0) mainDist = min(mainDist, distance(s1, s2, d1+1, d2) + 1);
    else mainDist = min(mainDist, distance(s1, s2, d1-1, d2) + 1);

    return mainDist;
}

int main() {
    
    long long s1, s2, d1, d2;

    while (cin >> s1 >> s2 >> d1 >> d2){
        if (s1 + s2 + d1 + d2 == 0) return 0;
        cout << calc(d1, d2, s1, s2) << endl;
    }

    return 0;
}