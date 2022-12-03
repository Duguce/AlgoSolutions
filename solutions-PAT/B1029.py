# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/12/1 18:30
# @File    : B1029.py
# @Software: PyCharm
################################################
# hint
# 旧键盘
################################################
def func():
    org_text = input().upper()
    actual_text = input().upper()
    ans = []
    for o in org_text:
        if o not in actual_text and o not in ans:
            ans.append(o)

    print(*ans, sep="")


if __name__ == '__main__':
    func()
