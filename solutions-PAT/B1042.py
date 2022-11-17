# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/17 22:03
# @File    : B1042.py
# @Software: PyCharm
################################################
# hint
# 字符统计
################################################
def func():
    text = input().lower().replace(" ", "")
    d = {}
    for t in text:
        if t.isalpha():
            if t not in d:
                d[t] = 1
            else:
                d[t] += 1

    d = sorted(d.items(), key=lambda x: (-x[1], x[0]))  # 对字典进行排序，值降序，键升序
    k, v = d[0]
    print(k, v, sep=" ")


if __name__ == '__main__':
    func()
