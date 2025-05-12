#include <stdio.h>
#include <math.h>

int isNarcissistic(int num)
{
    int original = num;
    int sum = 0;
    int digits = 0;
    int temp = num;

    while (temp != 0)
    {
        temp /= 10;
        digits++;
    }

    temp = num;
    while (temp != 0)
    {
        int digit = temp % 10;
        sum += pow(digit, digits);
        temp /= 10;
    }
    return sum == original;
}

int main()
{
    int T;
    scanf("%d", &T);

    while (T--)
    {
        int a, b;
        scanf("%d %d", &a, &b);

        int found = 0;
        for (int num = a; num <= b; num++)
        {
            if (isNarcissistic(num))
            {
                if (found)
                {
                    printf(" ");
                }
                printf("%d", num);
                found = 1;
            }
        }
        if (!found)
        {
            printf("-1");
        }
        printf("\n");
    }
    return 0;
}