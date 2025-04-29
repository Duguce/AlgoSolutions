#include <stdio.h>

#define MOD 100007

int main()
{
    int n;
    int dp[10001];
    dp[1] = 2;
    dp[2] = 3;

    for (int i = 3; i <= 10000; i++)
    {
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;
    }
    while (scanf("%d", &n) != EOF)
    {
        printf("%d\n", dp[n]);
    }
    return 0;
}