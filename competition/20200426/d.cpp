#include <bits/stdc++.h>
using namespace std;

int main(){

    int S;
    cin >> S;
    int n = 0;
    int S_n = S;

    while(S_n != 0){
        S_n /= 10;
        n++;
    }
    
    int ans = 0;
    for (int i = 0; i < n-3; i++){
        for (int j = i+4; j < n+1; j++){
            int num;
            num = (S/pow(10,n-j) - S/pow(10,n-i)*pow(10, j-i));
            if (num % 2019 == i){
                ans += 1;
            }
        }
    }

    cout << ans << endl;
}