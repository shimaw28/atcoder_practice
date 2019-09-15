#include <bits/stdc++.h>
#include <cmath>
#include <limits>
using namespace std;

int main()
{
    int n;
    int p;

    cin >> n >> p;

    if (n == 1)
    {
        cout << p << endl;
        exit();
    };

    int ans;
    ans = 1;
    float power;

    for (int i = 2; i <= p; i++)
    {
        power = pow(p, i);
        if (p % power == 0)
        {
            ans = i;
        };
        if (power >= p)
        {
            break;
        };
    };

    cout << ans << endl;
}