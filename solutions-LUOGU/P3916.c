#include <stdio.h>
#include <string.h>

#define MAXN 100005

int head[MAXN], to[MAXN * 2], nxt[MAXN * 2];
int tot = 0;

void addEdge(int u, int v)
{
    to[++tot] = v;
    nxt[tot] = head[u];
    head[u] = tot;
}

int ans[MAXN];
int vis[MAXN];

void dfs(int u, int val)
{
    if (ans[u] >= val)
        return;
    ans[u] = val;
    for (int i = head[u]; i; i = nxt[i])
    {
        int v = to[i];
        dfs(v, val);
    }
}

int main()
{
    int n, m;
    scanf("%d %d", &n, &m);

    for (int i = 1; i <= n; i++)
    {
        int u, v;
        scanf("%d %d", &u, &v);
        addEdge(v, u);
    }

    for (int i = n; i >= 1; i--)
    {
        if (ans[i] == 0)
        {
            dfs(i, i);
        }
    }

    for (int i = 1; i <= n; i++)
    {
        printf("%d ", ans[i]);
    }
    return 0;
}