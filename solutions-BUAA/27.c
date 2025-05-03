#include <stdio.h>

int main()
{
    long long n;

    while (scanf("%lld", &n) != EOF)
    {
        int t = 0;
        while (n != 1)
        {
            if (n % 2 == 0)
            {
                n /= 2;
            }
            else
            {
                n = 3 * n + 1;
            }
            t++;
        }
        printf("%d\n", t);
    }
    return 0;
}