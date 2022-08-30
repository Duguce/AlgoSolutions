# -*- coding: utf-8  -*-
import math

s, v = map(int, input().split())  # 输入路程和速度
workTime = math.ceil(s / v)  # 求得走路需要花费的时间并向上取整
totalTime = workTime + 10
deadline = 480  # 将时间数转化为分钟数（8:00 ==> 4800）
if totalTime <= deadline:
    startTime = deadline - totalTime
else:
    startTime = 1440 + deadline - totalTime

startHours = startTime // 60
startMinute = startTime % 60
print(f"{str(startHours).rjust(2, '0')}:{str(startMinute).rjust(2, '0')}")
