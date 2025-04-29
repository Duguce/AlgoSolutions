#include <stdio.h>

int solve(int a, int b)
{
    if (b == 0)
        return 0;

    if (a / b >= 2)
        return 1;

    return !solve(b, a % b);
}

int main()
{
    int a, b;

    while (scanf("%d %d", &a, &b) != EOF)
    {
        if (a < b)
        {
            int temp = a;
            a = b;
            b = temp;
        }

        if (solve(a, b))
        {
            printf("Nova\n");
        }
        else
        {
            printf("LaoWang\n");
        }
    }

    return 0;
}