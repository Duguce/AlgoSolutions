# -*- coding: utf-8  -*-
n, x = map(int, input().split(' '))
count = 0
for i in range(1, n + 1):
    if i >= 1000000 and i // 1000000 == x:
        count += 1
    if i >= 100000 and i // 100000 % 10 == x:
        count += 1
    if i >= 10000 and i // 10000 % 10 == x:
        count += 1
    if i >= 1000 and i // 1000 % 10 == x:
        count += 1
    if i >= 100 and i // 100 % 10 == x:
        count += 1
    if i >= 10 and i // 10 % 10 == x:
        count += 1
    if i % 10 == x:
        count += 1
print(count)
