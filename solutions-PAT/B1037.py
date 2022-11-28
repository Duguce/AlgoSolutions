# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/26 10:56
# @File    : B1037.py
# @Software: PyCharm
################################################
# hint
# 在霍格沃茨找零钱
################################################
def func():
    P, A = map(str, input().split())
    g1, s1, k1 = map(int, P.split("."))
    g2, s2, k2 = map(int, A.split("."))
    g3, s3, k3 = 0, 0, 0
    if g1 * 17 * 29 + s1 * 17 + k1 <= g2 * 17 * 29 + s2 * 17 + k2:  # 如果带的钱足够支付
        if k2 >= k1:
            k3 = k2 - k1
        else:
            k3 = k2 + 29 - k1
            s2 -= 1
        if s2 >= s1:
            s3 = s2 - s1
        else:
            s3 = s2 + 17 - s1
            g2 -= 1
        g3 = g2 - g1
        print(f"{g3}.{s3}.{k3}")
    else:
        if k1 >= k2:
            k3 = k1 - k2
        else:
            k3 = k1 + 29 - k2
            s1 -= 1
        if s1 >= s2:
            s3 = s1 - s2
        else:
            s3 = s1 + 17 - s2
            g1 -= 1
        g3 = g1 - g2
        print(f"-{g3}.{s3}.{k3}")


if __name__ == '__main__':
    func()
