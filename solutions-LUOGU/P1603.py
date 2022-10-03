# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/1 9:03
# @File    : P1603.py
# @Software: PyCharm

key = 'one two three four five six seven eight nine ten eleven twelve thirteen' \
      ' fourteen fifteen sixteen seventeen eighteen nineteen twenty a both another first second third'.split()  # 划分所有的键
value = [i for i in range(1, 21)]  # 构造1-20的值
value += [1, 2, 1, 1, 2, 3]  # 补充“a both another first second third”的值
value = [str(i ** 2 % 100).rjust(2, '0') for i in value]  # 对值进行平方取模
passwordDict = dict(zip(key, value))  # 构造字典
s = input().split()  # 获取输入
ans = [passwordDict[i] for i in s if i in passwordDict]

if ans == ['00'] * len(ans):
    print(0)
else:
    print(''.join(sorted(ans)).lstrip('0'))
