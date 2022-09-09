# -*- coding: utf-8  -*-
################################################
# hint
# 1.本题是求回文质数：方法1：逐个判断每个数是否是回文数质数；
# 方法2：打表法；
# 2.方法1解题思路（python3实现该思路可能会超时，但其他语言应该
# 没问题）：对范围内的数字进行遍历，判断是否是回文数和质数；
# 3.注意点1：善用质数和回文数的性质可以大大提高速度；
# 质数：偶数必定不是质数（除2以外）；
# 回文数：10的整数倍必定不是回文数；
# 注意点2：判断回文数的时候，可以考虑使用数学的方法（
# 而不是转字符串，会耗费更多的空间哈）
################################################
import math


def isPrime(n):
    """判断是否是质数"""
    if n % 2 == 0:
        return False
    return all(n % i != 0 for i in range(3, int(math.sqrt(n) + 1)))


def isPalindrome(n):
    """判断是否是回文数"""
    if n < 5 and n % 10 == 0:
        return False
    temp = n
    y = 0
    while temp != 0:
        y = y * 10 + temp % 10
        temp //= 10
    return n == y


a, b = map(int, input().split(' '))
for i in range(a, b + 1):
    if isPalindrome(i) and isPrime(i):
        print(i)

################################################
# 打表
################################################
# ans = [#制表脚本的值粘贴到此处#]
# a, b = map(int, input().split(' '))
# for i in ans:
#     if a <= i <= b:
#         print(i)
