#include <stdio.h>

int main()
{
    int n;
    int lst[1000007];
    long long count = 0;

    while (scanf("%d", &n) != EOF)
    {
        count = 0;
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
                    count++;
                }
            }
        }
        printf("%lld\n", count);
    }
    return 0;
}