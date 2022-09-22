# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/9/21 12:10
# @File    : P5734.py
# @Software: PyCharm
################################################
# hint
# emm...下面的思路在洛谷上没过，但是我下载了测试点之后
# 在本题的输出结果感觉没错呀
################################################
# q = int(input())  # 操作次数
# st = input()  # 输入初始字符串
# arr = []
# for i in range(q):
#     arr.append(input())
# for do in arr:
#     num = int(do[0])
#     st1 = do[2:]
#     if num == 1:
#         st = st + st1
#         print(st)
#     elif num == 2:  # 截取文档部分
#         num1 = int(st1[0])
#         num2 = int(st1[2]) + num1
#         st = st[num1:num2]
#         print(st)
#     elif num == 3:  # 插入片段
#         num1 = int(st1[0])
#         st2 = st1[2:] + st[num1:]
#         print(st[:num1] + st2)
#     elif num == 4:
#         try:
#             print(int(st.index(st1)))
#         except ValueError:
#             print(int(-1))
################################################
# hint
# 这个网上找的代码过了...但是本地测试感觉有点小问题
################################################
n = int(input())  # 一共有n次操作
str = input().rstrip()  # 读入原始字符串, 并删掉结尾的换行

for i in range(n):
    opt = input().split()  # 读入一行操作

    if opt[0] == '1':  # 后接文本
        str += opt[-1]
        print(str)
    elif opt[0] == '2':  # 截取文档部分
        str = str[int(opt[-2]): int(opt[-2]) + int(opt[-1])]
        print(str)
    elif opt[0] == '3':  # 插入片段
        str = str[:int(opt[-2])] + opt[-1] + str[int(opt[-2]):]
        print(str)
    else:  # 查找子串
        print(int(str.find(opt[-1])))
