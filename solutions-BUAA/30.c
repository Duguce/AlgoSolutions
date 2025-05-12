#include <stdio.h>

int gcd(int a, int b)
{
    while (b != 0)
    {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}

int main()
{
    int T;
    scanf("%d", &T);

    while (T--)
    {
        int a, b, c, d;
        scanf("%d %d %d %d", &a, &b, &c, &d);

        int numerator = a * d + b * c;
        int denominator = b * d;

        int g = gcd(numerator, denominator);
        numerator /= g;
        denominator /= g;

        printf("%d %d\n", numerator, denominator);
    }

    return 0;
}