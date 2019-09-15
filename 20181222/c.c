
#include <stdio.h>
#include <math.h>

int main(void)
{
    int n, p;
    
    scanf("%d %d", &n, &p);

    if (n == 1)
    {
        printf("%d", p);
        return 0;
    }

    int ans;
    ans = 1;

    for (int i = 2; i <= p; i++)
    {
        if ( p % (int) pow(i,  (double) n) == 0)
        {
            ans = i;
        }
        if (pow(i, (double) n) >  p)
        {
            break;
        }
    }

    printf("%d", ans);
    return 0;
}