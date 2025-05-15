#include <stdio.h>
#include <stdbool.h>

int n = 0;
int count = 0;

bool col[13];
bool diag1[25];
bool diag2[25];

void dfs(int row)
{
    if (row == n)
    {
        count++;
        return;
    }

    for (int i = 0; i < n; i++)
    {
        if (!col[i] && !diag1[row + i] && !diag2[row - i + n - 1])
        {
            col[i] = diag1[row + i] = diag2[row - i + n - 1] = true;
            dfs(row + 1);
            col[i] = diag1[row + i] = diag2[row - i + n - 1] = false;
        }
    }
}

int main()
{
    scanf("%d", &n);
    dfs(0);
    printf("%d\n", count);
    return 0;
}
