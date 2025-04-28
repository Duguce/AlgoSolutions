#include <stdio.h>

void hanoi(int n, char a, char b, char c)
{
    if (n == 1)
    {
        printf("%c to %c\n", a, c);
    }
    else
    {
        hanoi(n - 1, a, c, b);
        printf("%c to %c\n", a, c);
        hanoi(n - 1, b, a, c);
    }
}

int main()
{
    int n;
    int flag = 0;

    while (scanf("%d", &n) != EOF)
    {
        if (flag)
        {
            printf("\n");
        }
        flag = 1;
        hanoi(n, 'A', 'B', 'C');
    }
    return 0;
}
