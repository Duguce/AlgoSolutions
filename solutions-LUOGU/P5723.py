# -*- coding: utf-8  -*-
################################################
# hint
# 1.本题的本质是求 和小于等于某数的所有质数及质数的个数
# 2.解题思路：本题可以拆解为两个步骤，（1）判断是否是质数；
# （2）计算小于等于某数的所有质数及质数的个数
# 3.易错点1：容易忽略掉L的范围，即当L = 1的情况
################################################
import math


def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return all(n % i != 0 for i in range(3, int(math.sqrt(n) + 1)))


L = int(input())
isEnd = True
n = 0
primeNum = 0
primeSum = 0
while isEnd:
    if primeSum <= L and isPrime(n):
        print(n)
        primeNum += 1
        primeSum += n
    n += 1
    if primeSum + n > L:
        isEnd = False
print(primeNum)
