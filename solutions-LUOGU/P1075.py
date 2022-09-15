# -*- coding: utf-8  -*-
################################################
# hint
# 本题是一个质因数分解的问题，因为已知了n是两个质数的乘积，
# 只需要for循环从(n-1)枚举下去即可（并且不需要判断素数，这点
# 我上来想错了，太菜了害）,但这样用python3会超时
# 为解决python超时的方法，我们可以将for循环从2开始枚举，得到
# 的第一个因数，用n除以改因数，即可得到那个大的质数(注意要将其
# 转为整数)
################################################
import math

# def isPrime(n):
#     """判断一个数是否是质数"""
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(math.sqrt(n) + 1)):
#         if n % i == 0:
#             return False
#     return True

n = int(input())
for p in range(2, int(math.sqrt(n) + 1)):
    if n % p == 0:
        print(int(n / p))
        break
