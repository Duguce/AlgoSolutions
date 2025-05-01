#include <stdio.h>

int main()
{
    int n;
    int a, b, c;

    scanf("%d", &n);
    while (n--)
    {
        scanf("%d %d %d", &a, &b, &c);
        if (b <= c && b < a)
        {
            printf("fail\n");
        }
        else
        {
            int pos = 0;
            int hour = 0;

            while (pos < a)
            {
                pos += b;
                hour++;
                if (pos >= a)
                {
                    printf("%d\n", hour);
                    break;
                }
                pos -= c;
                if (pos < 0)
                {
                    pos = 0;
                }
            }
        }
    }
    return 0;
}