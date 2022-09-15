# -*- coding: utf-8  -*-
################################################
# hint
# 本题的解题思路是参考CSDN上的一个博主的思路，感觉很妙。
# 巧妙利用了元素集无序不重复的特性记录彩票序列，并对其进
# 行操作
################################################
n = int(input())  # 彩票张数
# set()函数可以创建一个无序不重复的元素集
awardNum = set(input().split())  # 中奖号码
mingNum = []  # 小明手上的彩票号码
awardCount = [0] * 7  # 各等级奖项中奖张数
for _ in range(n):
    num = len(set(input().split()) - awardNum)  # 找出两个元素集中不同的元素数量
    if num < 7:
        awardCount[num] += 1

print(*awardCount, sep=' ')

