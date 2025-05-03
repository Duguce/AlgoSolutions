#include <stdio.h>
#include <math.h>

int main()
{
    int x0, y0, z0;
    while (scanf("%d %d %d", &x0, &y0, &z0) == 3)
    {
        int n;
        int max_index = 0;
        double max_d_square = -1;

        scanf("%d", &n);

        for (int i = 1; i <= n; i++)
        {
            int x, y, z;
            scanf("%d %d %d", &x, &y, &z);
            int d_square = (x - x0) * (x - x0) + (y - y0) * (y - y0) + (z - z0) * (z - z0);
            if (d_square > max_d_square)
            {
                max_d_square = d_square;
                max_index = i;
            }
        }

        int k;
        scanf("%d", &k);
        double oil = sqrt(max_d_square) * k * 2;
        printf("%d %.6lf\n", max_index, oil);
    }
    return 0;
}