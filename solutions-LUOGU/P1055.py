# -*- coding: utf-8  -*-
isbn = input().strip()
temp = list(map(int, isbn.replace("-", "")[:9]))
num = sum(temp[i] * (i + 1) for i in range(len(temp)))
num %= 11
if num == 10:
    num = "X"
if str(num) == isbn[-1]:
    print("Right")
else:
    isbn = isbn[:12] + str(num)
    print(isbn)