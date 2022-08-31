# -*- coding: utf-8  -*-
a, b, c = map(int, input().split(' '))
if a <= b <= c:
    print(a, b, c, sep=' ')
elif a <= c <= b:
    print(a, c, b, sep=' ')
elif b <= a <= c:
    print(b, a, c, sep=' ')
elif b <= c <= a:
    print(b, c, a, sep=' ')
elif c <= a <= b:
    print(c, a, b, sep=' ')
else:
    print(c, b, a, sep=' ')
