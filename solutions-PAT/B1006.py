# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/17 21:11
# @File    : B1006.py
# @Software: PyCharm
################################################
# hint
# 换个格式输出整数
################################################
def func():
    n = int(input())
    s = (n // 100) * "B" + (n % 100 // 10) * "S" + "".join(map(str, range(1, n % 10 + 1)))
    print(s)


if __name__ == '__main__':
    func()
