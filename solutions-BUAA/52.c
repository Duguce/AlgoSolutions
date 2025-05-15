#include <stdio.h>

#define INF 1e9
#define MAXN 505

int graph[MAXN][MAXN];

int min(int a, int b)
{
    if (a < b)
    {
        return a;
    }
    else
    {
        return b;
    }
}

void floydWarshall(int n)
{
    for (int k = 0; k < n; k++)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (graph[i][k] < INF && graph[k][j] < INF)
                {
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
                }
            }
        }
    }
}

int main()
{
    int n, q;
    while (scanf("%d %d", &n, &q) != EOF)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                int x;
                scanf("%d", &x);
                if (x == -1)
                {
                    graph[i][j] = INF;
                }
                else
                {
                    graph[i][j] = x;
                }
            }
        }

        floydWarshall(n);

        for (int i = 0; i < q; i++)
        {
            int u, v;
            scanf("%d %d", &u, &v);
            u--;
            v--;
            if (graph[u][v] == INF || u == v)
            {
                printf("jujue\n");
            }
            else
            {
                printf("%d\n", graph[u][v]);
            }
        }
    }
    return 0;
}
