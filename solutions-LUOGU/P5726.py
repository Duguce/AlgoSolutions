# -*- coding: utf-8  -*-
################################################
# hint
# 本题是一个打分问题（需去掉一个最高分和一个最低分，然后
# 求平均值），思路很简单，遍历列表score所有元素，求出所
# 有得分和以及最大得分和最小得分，然后求平均值
################################################
n = int(input())
score = list(map(int, input().split(' ')))
maxScore = 0
minScore = 10
ans = 0
average = 0
for i in score:
    ans += i
    if i > maxScore:
        maxScore = i
    elif i < minScore:
        minScore = i
print("%.2f" % ((ans - maxScore - minScore) / (len(score) - 2)))
