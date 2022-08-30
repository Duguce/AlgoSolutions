# -*- coding: utf-8  -*-
def solution():
    s = list(range(9))
    for a in range(100, 333):
        b = 2 * a
        c = 3 * a
        s[0] = a / 100
        s[1] = a % 100 / 10
        s[2] = a % 10
        s[3] = b / 100
        s[4] = b % 100 / 10
        s[5] = b % 10
        s[6] = c / 100
        s[7] = c % 100 / 10
        s[8] = c % 10
        n = 1
        q = 0
        for item in s:
            item = int(item)
            n *= item
            q += item
        if n == 362880 and q == 45:
            print(a, b, c, sep=" ")


solution()
