# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/25 8:52
# @File    : P1177.py
# @Software: PyCharm
# def quick_sort(lst):
#     """该法的空间复杂度较高，当n较大时，部分测试点内存会超过上限"""
#     if len(lst) < 2:
#         return lst
#     pivot = lst[0]
#     less = [i for i in lst[1:] if i <= pivot]
#     greater = [i for i in lst[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)
def quick_sort(lst, left, right):
    if left >= right:
        return
    i, k = partition(lst, left, right)
    if left < i:
        quick_sort(lst, left, i)
    if k + 1 < right:
        quick_sort(lst, k + 1, right)


def partition(lst, left, right):
    mid = left + (right - left) // 2
    lst[mid], lst[right] = lst[right], lst[mid]
    pivot = lst[right]
    i = left - 1
    k = i
    for j in range(left, right):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
            k += 1
            if i < k:
                lst[k], lst[j] = lst[j], lst[k]
        elif lst[j] == pivot:
            k += 1
            lst[k], lst[j] = lst[j], lst[k]
    k += 1
    lst[k], lst[right] = lst[right], lst[k]
    return i, k


def func():
    n = int(input())
    lst = list(map(int, input().split()))
    quick_sort(lst, 0, n - 1)
    print(*lst, sep=" ")


if __name__ == '__main__':
    func()
