#include <stdio.h>

int main()
{
    char num[100005];
    scanf("%s", num);

    int sum = 0;
    for (int i = 0; num[i] != '\0'; i++)
    {
        sum += num[i] - '0';
    }

    while (sum >= 10)
    {
        int temp = 0;
        while (sum > 0)
        {
            temp += sum % 10;
            sum /= 10;
        }
        sum = temp;
    }

    printf("%d\n", sum);
    return 0;
}