# -*- coding: utf-8  -*-
a, b, c, d = map(int, input().split(" "))
swimHour = c - a
if d >= b:
    swimMinute = d - b
else:
    swimMinute = d + 60 - b
    swimHour = swimHour - 1
print(swimHour, swimMinute, sep=" ")
