# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/26 10:31
# @File    : B1036.py
# @Software: PyCharm
################################################
# hint
# 跟奥巴马一起编程
################################################
def func():
    n, c = input().split()
    n = int(n)
    row = int((n + 1) / 2)  # 确定要打印的行数
    print(str(c) * n)
    for i in range(row - 2):
        print(str(c) + " " * (n - 2) + str(c))
    print(str(c) * n)


if __name__ == '__main__':
    func()
