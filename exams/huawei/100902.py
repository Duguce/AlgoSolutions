################################################
# hint
# 机试题2：软件安装工具
################################################
from collections import defaultdict, deque


def min_install_time(N, times, dependencies):
    graph = defaultdict(list)
    in_degree = [0] * (N + 1)

    for i, deps in enumerate(dependencies, 1):
        for dep in deps:
            if dep != -1:
                graph[dep].append(i)
                in_degree[i] += 1

    queue = deque([i for i in range(1, N + 1) if in_degree[i] == 0])
    dp = [0] * (N + 1)

    while queue:
        node = queue.popleft()
        dp[node] += times[node - 1]

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            dp[neighbor] = max(dp[neighbor], dp[node])
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return max(dp)


def func():
    N = int(input())
    times = list(map(int, input().split()))
    dependencies = [list(map(int, input().split())) for _ in range(N)]

    result = min_install_time(N, times, dependencies)
    print(result)


if __name__ == '__main__':
    func()
