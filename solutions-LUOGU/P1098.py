# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/19 16:22
# @File    : P1098.py
# @Software: PyCharm
################################################
# hint
# 模拟题：字符串的展开
################################################
def func():
    param1, param2, param3 = map(int, input().split())
    s = list(input())
    for i in range(1, len(s) - 1):
        left = s[i - 1]
        right = s[i + 1]
        if s[i] == '-' and ((left.isdigit() and right.isdigit()) or (left.islower() and right.islower())) and ord(
                right) > ord(left):
            temp = ""
            for j in range(ord(left) + 1, ord(right)):
                temp += chr(j) * param2
            if param3 == 2:
                temp = temp[::-1]
            if param1 == 2 and left.isalpha():
                temp = temp.upper()
            if param1 == 3:
                temp = "*" * len(temp)
            s[i] = temp
    print(*s, sep="")


if __name__ == '__main__':
    func()
