# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2023/1/7 10:06
# @File    : JZ09.py
# @Software: PyCharm
################################################
# hint
# 面试题9：用两个栈实现队列
################################################
class CQueue:
    def __init__(self):
        self.stk_in = []
        self.stk_out = []

    def appendTail(self, value: int) -> None:
        self.stk_in.append(value)

    def deleteHead(self) -> int:
        if self.stk_out == []:
            while self.stk_in != []:
                self.stk_out.append(self.stk_in.pop())
        if self.stk_out != []:
            return self.stk_out.pop()
        else:
            return -1
