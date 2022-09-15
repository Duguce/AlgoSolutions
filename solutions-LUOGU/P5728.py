# -*- coding: utf-8  -*-
################################################
# hint
# 本题用两层循环模拟一下
################################################
n = int(input())
students = []
count = 0  # 记录“旗鼓相当的对手”的对数
for _ in range(n):
    s = list(map(int, input().split(' ')))
    students.append(s)
for i in range(n):
    for j in range(i + 1, n):
        if abs(students[i][0] - students[j][0]) <= 5 and abs(students[i][1] - students[j][1]) <= 5 and abs(
                students[i][2] - students[j][2]) <= 5 and abs(sum(students[i]) - sum(students[j])) <= 10:
            count += 1
print(count)
