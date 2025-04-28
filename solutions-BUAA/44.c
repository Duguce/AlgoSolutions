#include <stdio.h>

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

int main()
{
    int a, b;
    while (scanf("%d %d", &a, &b) != EOF)
    {
        swap(&a, &b);
        printf("%d %d\n", a, b);
    }
    return 0;
}