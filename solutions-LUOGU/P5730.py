# -*- coding: utf-8  -*-
################################################
# hint
# 本题不多说，看代码(划水了)
################################################
def hanshu(i, j):
    if i == 1 and j in [0, 2, 3, 5, 6, 7, 8, 9]:
        return "XXX"
    elif i == 1 and j == 1:
        return "..X"
    elif i == 1 and j == 4:
        return "X.X"
    elif i == 2 and j in [0, 4, 8, 9]:
        return "X.X"
    elif i == 2 and j in [1, 2, 3, 7]:
        return "..X"
    elif i == 2 and j in [5, 6]:
        return "X.."
    elif i == 3 and j == 0:
        return "X.X"
    elif i == 3 and j in [1, 7]:
        return "..X"
    elif i == 3 and j in [2, 3, 4, 5, 6, 8, 9]:
        return "XXX"
    elif i == 4 and j in [0, 6, 8]:
        return "X.X"
    elif i == 4 and j in [1, 3, 4, 5, 7, 9]:
        return "..X"
    elif i == 4 and j == 2:
        return "X.."
    elif i == 5 and j in [0, 2, 3, 5, 6, 8, 9]:
        return "XXX"
    elif i == 5 and j in [1, 4, 7]:
        return "..X"


n = int(input())
m = list(map(int, input().strip()))
for i in range(1, 6):
    x = []
    for j in m:
        x.append(hanshu(i, j))
    print(".".join(x))
