#include <stdio.h>

int main()
{
    int T;
    scanf("%d", &T);
    while (T--)
    {
        int a, b, c, d, e, f, g, h;
        scanf("%d %d %d %d %d %d %d %d", &a, &b, &c, &d, &e, &f, &g, &h);
        int first = a / (b * c);
        int second = (d / e) / (f * g);
        int ans = first + second * h;
        printf("%d\n", ans);
    }
    return 0;
}