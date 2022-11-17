# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/17 20:48
# @File    : B1056.py
# @Software: PyCharm
################################################
# hint
# 组合数的和
################################################
def func():
    n, *nums = input().split()  # 分别存储输入的数字个数及数字内容
    lst = []  # 定义一个数组用来存储组合数
    for i in range(int(n)):  # 遍历每一个数字
        t = nums[i]
        for j in range(int(n)):
            g = nums[j]
            if t != g:
                lst.append(t + g)
    ans = sum(list(map(int, lst)))
    print(ans)


if __name__ == '__main__':
    func()
