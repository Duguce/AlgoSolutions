#include <stdio.h>

int main()
{
    int n;
    int lst[1000007];

    while (scanf("%d", &n) != EOF)
    {
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &lst[i]);
        }

        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if (lst[i] > lst[j])
                {
                    int temp = lst[i];
                    lst[i] = lst[j];
                    lst[j] = temp;
                }
            }
        }

        for (int i = 0; i < n; i++)
        {
            printf("%d ", lst[i]);
        }

        printf("\n");
    }

    return 0;
}