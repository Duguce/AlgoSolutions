# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/9/21 18:04
# @File    : P1308.py
# @Software: PyCharm
target = input()  # 接收目标词
target = target.lower()  # 转换为小写
sentence = input()  # 输入文本
word = []  # 每次提取文本中的一个单词
ans = 0
firstPos = -1
for i in range(len(sentence)):  # 将句子中的单词全转换为小写
    if sentence[i] != ' ':  # 单个单词未结束
        word.append(sentence[i].lower())
    else:  # 分析word中的一个完整的单词
        if list(target) == word:  # 目标字符和提取的单词相同
            ans += 1
            if firstPos == -1:
                firstPos = i - len(target)
        word.clear()  # 清楚当前单词，准备下一个单词
if ans > 0:
    print(ans, firstPos, sep=' ')
else:
    print(-1)
