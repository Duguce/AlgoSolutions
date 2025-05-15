#include <stdio.h>

int main()
{
    int coin[6];
    int value[6] = {1, 5, 10, 50, 100, 500};

    while (scanf("%d %d %d %d %d %d", &coin[0], &coin[1], &coin[2], &coin[3], &coin[4], &coin[5]) != EOF)
    {
        int amount;
        scanf("%d", &amount);

        int count = 0;

        for (int i = 5; i >= 0; i--)
        {
            int use = amount / value[i];
            if (use > coin[i])
            {
                use = coin[i];
            }
            amount -= use * value[i];
            count += use;
        }
        printf("%d\n", count);
    }
    return 0;
}
