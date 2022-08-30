# -*- coding: utf-8  -*-
import math


def main():
    T = int(input())
    if T == 1:
        print("I love Luogu!")
    elif T == 2:
        print(6, 4, sep=" ")
    elif T == 3:
        print(3, 12, 2, sep="\n")
    elif T == 4:
        print("%.6g" % (500 / 3))
    elif T == 5:
        print(int((260 + 220) / (12 + 20)))
    elif T == 6:
        print(math.sqrt(6 * 6 + 9 * 9))
    elif T == 7:
        print(100 + 10, 100 + 10 - 20, 0, sep="\n")
    elif T == 8:
        print(2 * 3.141593 * 5, 3.141593 * 5 * 5, 4 / 3 * 3.141593 * 5 * 5 * 5 * 1.0, sep='\n')
    elif T == 9:
        print(22)
    elif T == 10:
        print(9)
    elif T == 11:
        print(100 / 3 * 1.0)
    elif T == 12:
        print(ord('M') - ord('A') + 1)
        print(chr(ord('A') + 17))
    elif T == 13:
        print(round(pow(4 / 3 * 3.141593 * (4 * 4 * 4 + 10 * 10 * 10), 1.0 * 1 / 3)))
    elif T == 14:
        print(50)


main()
