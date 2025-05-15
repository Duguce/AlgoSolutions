#include <stdio.h>

int main()
{
    char id[9];
    scanf("%s", id);

    int weights[] = {9, 8, 7, 6, 5, 4, 3, 2, 1};
    int sum = 0;

    for (int i = 0; i < 8; i++)
    {
        int digit = id[i] - '0';
        sum += digit * weights[i];
    }
    int check_digit = sum % 10;
    printf("%s%d", id, check_digit);

    return 0;
}