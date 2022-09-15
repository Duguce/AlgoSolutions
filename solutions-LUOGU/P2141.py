# -*- coding: utf-8  -*-
################################################
# hint
# 本题用两层循环模拟一下，但请注意我的两层循环中含重复值
# 因此，如果直接计数得到的结果会大于正确结果。因此，我引
# 入了一个n维的ansArr数组，当Arr的某个元素是其他两个不
# 同元素之和时，则将对应位置的ansArr元素值转为1，最后统
# 计ansArr中1的个数即可
################################################
n = int(input())
arr = list(map(int, input().split()))
ans = 0
ansArr = [0] * n
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] in arr:
            index = arr.index(arr[i] + arr[j])
            ansArr[index] = 1

for k in ansArr:
    if k == 1:
        ans += 1

print(ans)
