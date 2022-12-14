# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/12/13 14:10
# @File    : JZ05.py
# @Software: PyCharm
################################################
# hint
# 面试题5：替换空格
################################################
class Solution:
    # 方法一：创建一个新的字符串
    # def replaceSpace(self, s: str) -> str:
    #     ans = ""
    #     for c in s:
    #         if c != " ":
    #             ans += c
    #         else:
    #             ans += "%20"
    #     return ans

    # 方法二：先用split(" ")以空格为单位进行拆分，然后再利用"%20".join(s)对字符串进行拼接
    # def replaceSpace(self, s: str) -> str:
    #     s = s.split(" ")
    #     return "%20".join(s)

    # 方法三：双指针，倒序替换
    def replaceSpace(self, s: str) -> str:
        if not s:
            return s
        orig_len = len(s)  # 字符串s的实际长度
        counter = s.count(" ")  # 计算字符串中空格的数量
        new_len = orig_len + counter * 2  # 空格替换后的长度
        index_of_orig = orig_len - 1
        index_of_new = new_len - 1
        res = list(s)
        res.extend([" "] * counter * 2)
        while 0 <= index_of_orig < index_of_new:
            if res[index_of_orig] != " ":
                res[index_of_new] = res[index_of_orig]
                index_of_new -= 1
            else:
                res[index_of_new - 2:index_of_new + 1] = '%20'
                index_of_new -= 3
            index_of_orig -= 1
        return "".join(res)


if __name__ == '__main__':
    # --------------------测试用例-------------------- #
    sol = Solution()
    print(sol.replaceSpace("We are happy."))
