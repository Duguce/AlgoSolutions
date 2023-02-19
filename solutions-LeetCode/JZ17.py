# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2023/2/17 11:01
# @File    : JZ17.py
# @Software: PyCharm
################################################
# hint
# 面试题17：打印从1到最大的n位数
################################################
class Solution:
    def printNumbers(self, n: int) -> [int]:
        def dfs(x):
            if x == n:
                s = ''.join(num[self.start:])
                if s != '0': res.append(int(s))
                if n - self.start == self.nine: self.start -= 1
                return
            for i in range(10):
                if i == 9: self.nine += 1
                num[x] = str(i)
                dfs(x + 1)
            self.nine -= 1

        num, res = ['0'] * n, []
        self.nine = 0
        self.start = n - 1
        dfs(0)
        return res


if __name__ == '__main__':
    # --------------------测试用例1-------------------- #
    sol = Solution()
    print(sol.printNumbers(1))
