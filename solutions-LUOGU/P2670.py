# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/13 9:24
# @File    : P2670.py
# @Software: PyCharm
################################################
# hint
# 数据量比较小，硬模拟就完事儿了
################################################
def func():
    n, m = map(int, input().split())
    maps = [list(input()) for _ in range(n)]
    for x in range(n):
        for y in range(m):
            count = 0
            if maps[x][y] == "?":
                if x - 1 >= 0 and maps[x - 1][y] == "*":
                    count += 1
                if x - 1 >= 0 and y - 1 >= 0 and maps[x - 1][y - 1] == "*":
                    count += 1
                if x + 1 <= n - 1 and maps[x + 1][y] == "*":
                    count += 1
                if x + 1 <= n - 1 and y + 1 <= m - 1 and maps[x + 1][y + 1] == "*":
                    count += 1
                if y - 1 >= 0 and maps[x][y - 1] == "*":
                    count += 1
                if x + 1 <= n - 1 and y - 1 >= 0 and maps[x + 1][y - 1] == "*":
                    count += 1
                if y + 1 <= m - 1 and maps[x][y + 1] == "*":
                    count += 1
                if x - 1 >= 0 and y + 1 <= m - 1 and maps[x - 1][y + 1] == "*":
                    count += 1
                maps[x][y] = count

    for row in maps:
        print(*row, sep="")


if __name__ == '__main__':
    func()
