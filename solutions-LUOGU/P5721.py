# -*- coding: utf-8  -*-
n = int(input())
m = 0
for i in range(n + 1, 1, -1):
    for _ in range(1, i):
        m += 1
        print(str(m).zfill(2), end='')
    print()