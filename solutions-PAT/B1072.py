# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/12/2 8:11
# @File    : B1072.py
# @Software: PyCharm
################################################
# hint
# 开学寄语
################################################
def func():
    n, m = map(int, input().split())
    lim_lst = input().split()
    stu_lst = [input().split() for _ in range(n)]
    dic = {}  # 存储被查获的学生及对应物品
    people, things = 0, 0  # 存储携带违规物品的学生数量及对应的违规物品数量
    for i in range(n):
        for l in stu_lst[i][2:]:
            if l in lim_lst and stu_lst[i][0] not in dic.keys():
                dic[stu_lst[i][0]] = l
                people += 1
                things += 1
            elif stu_lst[i][0] in dic.keys() and l in lim_lst:
                dic[stu_lst[i][0]] = dic[stu_lst[i][0]] + " " + l
                things += 1

    for k, v in dic.items():
        print("%s: %s" % (k, v))
    print(people, things)


if __name__ == '__main__':
    func()
