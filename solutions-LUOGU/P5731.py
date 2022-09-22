# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/9/17 8:38
# @File    : P5731.py
# @Software: PyCharm
################################################
# hint
# 本题卡了很久，想到的思路就是模拟，一碰边或者前边的数已
# 填充就向右转，不过细节思路没想清楚，去csdn上找了一篇
# 题解看了一下，很妙！
################################################
n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
x = 0
y = 0
towards = ['y=y+1', 'x+=1', 'y-=1', 'x-=1']
t = 0
for i in range(1, n * n + 1):
    arr[x][y] = i
    exec(towards[t])  # 执行列表中第t个元素的操作
    if x > n - 1 or y > n - 1 or arr[x][y] != 0:  # 当到达列表边缘或者前面的元素值不等于0时
        exec(towards[(t + 2) % 4])  # 退一步
        t = (t + 1) % 4  # 调整方向
        exec(towards[t])  # 再进一步

for i in arr:
    for j in i:
        print(f"{j: >3}", end='')
    print()
