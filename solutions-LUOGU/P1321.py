# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/9/30 8:22
# @File    : P1321.py
# @Software: PyCharm
s = input()  # 输入字符串
girlCount = 0
boyCount = 0
for i in range(len(s)-2):
    if s[i] == 'b' or s[i+1] == 'o' or s[i+2] == 'y':
        boyCount += 1

for i in range(len(s)-3):
    if s[i] == 'g' or s[i + 1] == 'i' or s[i + 2] == 'r' or s[i + 3] == 'l':
        girlCount += 1
print(boyCount, girlCount, sep='\n')
