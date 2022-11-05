# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/11/1 22:51
# @File    : B1001.py
# @Software: PyCharm
################################################
# hint
# 害死人不偿命的(3n+1)猜想
################################################
def func():
    n = int(input())
    ans = 0  # 记录从n到1需要的步数
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (3 * n + 1) / 2
        ans += 1
    print(ans)


if __name__ == '__main__':
    func()
