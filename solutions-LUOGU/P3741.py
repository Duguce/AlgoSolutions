# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/9/22 10:53
# @File    : P3741.py
# @Software: PyCharm

n = int(input())  # 输入的字符串的长度
s = input()  # 输入的字符串
s = s.replace('VK', '1')
ans = 0
for i in s:
    if i == '1':
        ans += 1
if ("VV" in s) or ("KK" in s):
    ans += 1
print(ans)
