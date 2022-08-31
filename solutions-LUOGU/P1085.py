# -*- coding: utf-8  -*-
print(max(__import__('itertools').chain(((i, sum(map(int, input().split(' ')))) for i in range(1, 8)), ((0, 9),)),
          key=lambda x: x[1])[0])
