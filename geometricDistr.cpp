#Day 4
#Geometric Distribution C++14



#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int a,b,c;
    cin >> a >> b >> c;
    double z = double(a)/b;
    double geoD = z * pow(1.0 - z, double(c-1));
    cout.precision(3);
    cout << fixed << geoD;
    return 0;
}

