# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/18 14:57
# @File    : B1061.py
# @Software: PyCharm
################################################
# hint
# 判断题
################################################
def func():
    n, m = map(int, input().split())
    scores = list(map(int, input().split()))  # 记录每个题的分值
    answers = input().split()  # 记录每个题的正确答案
    stu = [input().split() for _ in range(n)]  # 记录每个学生的作答
    for s in stu:  # 遍历每个学生的作答
        stu_score = 0  # 定义每个学生的初始成绩
        for j in range(m):  # 检查学生每道题的答案
            if answers[j] == s[j]:  # 若学生答案与正确答案相同，则加上该题的分值
                stu_score += scores[j]
        print(stu_score)  # 输出当前学生的分数


if __name__ == '__main__':
    func()
