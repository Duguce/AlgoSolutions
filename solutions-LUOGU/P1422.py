# -*- coding: utf-8  -*-
x = int(input())
charge = 0
if x <= 150:
    charge = x * 0.4463
elif 151 <= x <= 400:
    charge = (x - 150) * 0.4663 + 150 * 0.4463
elif x >= 401:
    charge = (x - 400) * 0.5663 + (400 - 150) * 0.4663 + 150 * 0.4463
print("%.1f" % charge)
