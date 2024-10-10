################################################
# hint
# 机试题1：铺设光缆问题
################################################
from collections import deque


def shortest_distance(m, n, start, end, obstacles):
    grid = [[0] * m for _ in range(n)]
    for x, y in obstacles:
        grid[y][x] = 1

    queue = deque([(start[1], start[0], 0)])
    visited = set([(start[1], start[0])])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        y, x, dist = queue.popleft()
        if (y, x) == (end[1], end[0]):
            return dist

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == 0 and (ny, nx) not in visited:
                queue.append((ny, nx, dist + 1))
                visited.add((ny, nx))

    return -1


def func():
    m, n = map(int, input().split())
    a1, a2 = map(int, input().split())
    b1, b2 = map(int, input().split())
    k = int(input())
    obstacles = [tuple(map(int, input().split())) for _ in range(k)]

    result = shortest_distance(m, n, (a1, a2), (b1, b2), obstacles)
    print(result)


if __name__ == '__main__':
    func()
