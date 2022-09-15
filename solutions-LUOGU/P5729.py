# -*- coding: utf-8  -*-
w, x, h = map(eval, input().split(' '))
v = [[['1' for k in range(h)] for j in range(x)] for i in range(w)]
q = eval(input())
ans = 0

for _ in range(q):
    x1, y1, z1, x2, y2, z2 = map(eval, input().split(' '))
    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            for k in range(z1 - 1, z2):
                v[i][j][k] = '0'

print(str(v).count('1'))
