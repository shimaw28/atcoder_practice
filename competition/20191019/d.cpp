#include <bits/stdc++.h>
using namespace std;

void foreach_permutation(int n, std::function<void(int *)> f)
{
    int indexes[n];
    for (int i = 0; i < n; i++)
        indexes[i] = i;
    do
    {
        f(indexes);
    } while (std::next_permutation(indexes, indexes + n));
}

int main() {
    int N;
    cin >> N;
    vector<int> data(5);
    for (int i=0; i<5; i++){
        cin >> data.at(i);
    }

    int ans;
    ans = 0;

    foreach_permutation(3, [](int *indexes){
        int a, b, c;
        a = indexes[0];
        b = indexes[1];
        c = indexes[2];

        if (a<b+c || b<c+a || c<a+b){
            ans += 1;
        }
    });

    cout << ans;
}