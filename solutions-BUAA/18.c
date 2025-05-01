#include <stdio.h>

int main()
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    double avg = (a + b + c) / 3.0;
    printf("%.2f\n", avg);

    return 0;
}