# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/20 8:27
# @File    : P1786.py
# @Software: PyCharm
################################################
# hint
# 模拟，两次排序
################################################
def func():
    n = int(input())
    persons = [[i] + input().split() for i in range(n)]
    for i in range(3):
        print(persons[i][1], persons[i][2], persons[i][4])
    persons = persons[3:]
    persons.sort(key=lambda x: int(x[3]), reverse=True)  # 副帮主以下先按照帮贡、等级排序
    for i in range(n - 3):  # 重新分配职位
        if 0 <= i <= 1:
            persons[i][2] = "HuFa"
        elif 2 <= i <= 5:
            persons[i][2] = "ZhangLao"
        elif 6 <= i <= 12:
            persons[i][2] = "TangZhu"
        elif 13 <= i <= 37:
            persons[i][2] = "JingYing"
        else:
            persons[i][2] = "BangZhong"
    dic = {"HuFa": 1, "ZhangLao": 2, "TangZhu": 3, "JingYing": 4, "BangZhong": 5}  # 定义字典，辅助排序
    persons.sort(key=lambda x: (dic[x[2]], -int(x[4]), x[0]))
    for person in persons:
        print(person[1], person[2], person[4])


if __name__ == '__main__':
    func()
