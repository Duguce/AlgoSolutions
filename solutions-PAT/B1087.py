# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/8 10:41
# @File    : B1087.py
# @Software: PyCharm
################################################
# hint
# 有多少不同的值
################################################
def func():
    n = int(input())
    st = set()  # 用以记录⌊n/2⌋+⌊n/3⌋+⌊n/5⌋的值
    for i in range(1, n + 1):
        curr = int(i / 2) + int(i / 3) + int(i / 5)
        st.add(curr)
    print(len(st))


if __name__ == '__main__':
    func()
