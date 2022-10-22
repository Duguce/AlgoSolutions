# -*- coding: utf-8  -*-
# @Author  : Duguce 
# @Email   : zhgyqc@163.com
# @Time    : 2022/10/17 9:30
# @File    : P1518.py
# @Software: PyCharm
################################################
# hint
# 模拟问题，坐标边界判断，转向...
################################################
def func():
    mapArr = []  # 定义一个数组用来记录地图信息
    t = 0  # 定义初始时间
    f_x, f_y = 0, 0
    c_x, c_y = 0, 0
    for i in range(10):  # 录入地图信息
        mapArr.append(input())
        for j in range(10):
            if mapArr[i][j] == "F":
                f_x, f_y = i, j  # 记录Farmer John的初始位置
            if mapArr[i][j] == "C":
                c_x, c_y = i, j  # 记录两头牛的初始位置

    f_toward, c_toward = 1, 1  # 定义两者的初始朝向
    while f_x != c_x or f_y != c_y:
        # 记录每时刻Farmer John的位置
        if f_toward == 1:
            if f_x - 1 < 0 or mapArr[f_x - 1][f_y] == "*":  # 如果越界或碰壁就转向
                f_toward = 2
            else:
                f_x -= 1
        elif f_toward == 2:
            if f_y + 1 > 9 or mapArr[f_x][f_y + 1] == "*":
                f_toward = 3
            else:
                f_y += 1
        elif f_toward == 3:
            if f_x + 1 > 9 or mapArr[f_x + 1][f_y] == "*":
                f_toward = 4
            else:
                f_x += 1
        else:
            if f_y - 1 < 0 or mapArr[f_x][f_y - 1] == "*":
                f_toward = 1
            else:
                f_y -= 1
        # 记录每时刻牛的位置
        if c_toward == 1:
            if c_x - 1 < 0 or mapArr[c_x - 1][c_y] == "*":  # 如果越界或碰壁就转向
                c_toward = 2
            else:
                c_x -= 1
        elif c_toward == 2:
            if c_y + 1 > 9 or mapArr[c_x][c_y + 1] == "*":
                c_toward = 3
            else:
                c_y += 1
        elif c_toward == 3:
            if c_x + 1 > 9 or mapArr[c_x + 1][c_y] == "*":
                c_toward = 4
            else:
                c_x += 1
        else:
            if c_y - 1 < 0 or mapArr[c_x][c_y - 1] == "*":
                c_toward = 1
            else:
                c_y -= 1

        t += 1
        if t >= 100000:
            print(0)  # 如果足够时间之后还是没有抓到，那么就输出0，并结束程序
            exit(0)
    print(t)


if __name__ == '__main__':
    func()
