#include <stdio.h>
#include <string.h>

int main()
{
    int T;
    scanf("%d", &T);

    while (T--)
    {
        int n, m;
        scanf("%d %d", &n, &m);

        int row = 1, col = 1;
        int out_of_bounds = 0;

        for (int i = 0; i < m; i++)
        {
            char dir;
            int k;
            scanf(" %c %d", &dir, &k);

            if (dir == 'U')
            {
                row -= k;
            }
            else if (dir == 'D')
            {
                row += k;
            }
            else if (dir == 'L')
            {
                col -= k;
            }
            else if (dir == 'R')
            {
                col += k;
            }

            if (row < 1 || row > n || col < 1 || col > n)
            {
                out_of_bounds = 1;
            }
        }

        if (out_of_bounds)
        {
            printf("WanQuanGaoBuDong!\n");
        }
        else
        {
            int position = (col - 1) * n + row;
            printf("%d\n", position);
        }
    }
    return 0;
}