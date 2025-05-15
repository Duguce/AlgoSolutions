#include <stdio.h>
#include <math.h>

int isPrime(long long n)
{
    if (n < 2)
    {
        return 0;
    }

    for (long long i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    long long n;
    while (scanf("%lld", &n) != EOF)
    {
        if (isPrime(n))
        {
            printf("jhljx is good!\n");
        }
        else
        {
            printf("jhljx is sangxinbingkuang!\n");
        }
    }
    return 0;
}