# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/30 9:29
# @File    : B1076.py
# @Software: PyCharm
################################################
# hint
# Wifi密码
################################################
def func():
    n = int(input())
    lst = [input().split() for _ in range(n)]
    dic = {"A": "1", "B": "2", "C": "3", "D": "4"}
    ans = ""
    for l in lst:
        for m in l:
            if m[-1] == "T":
                ans += dic[m[0]]
                break
    print(ans)


if __name__ == '__main__':
    func()
