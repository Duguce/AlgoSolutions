# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/18 8:18
# @File    : B1047.py
# @Software: PyCharm
################################################
# hint
# 编程团体赛
################################################
def func():
    n = int(input())  # 记录队伍数
    teamId, score = [], []  # 分别记录队伍编号和成绩
    teamScore = {}  # 记录队伍编号及对应总成绩
    topTeam, topScore = "", 0  # 记录冠军队编号和总成绩
    temp = [input().split() for _ in range(n)]  # 暂存输入队伍信息
    for i in range(n):
        score = int(temp[i][1])  # 暂存成绩
        teamId = temp[i][0].split("-")[0]  # 暂存团队编号
        if teamId not in teamScore:
            teamScore[teamId] = score
        else:
            teamScore[teamId] += score
    for t in teamScore:
        if teamScore[t] > topScore:
            topScore = teamScore[t]
            topTeam = t

    print(topTeam, topScore, sep=" ")


if __name__ == '__main__':
    func()
