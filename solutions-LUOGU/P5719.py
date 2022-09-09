n, k = map(int, input().split(' '))
countA = 0
sumA = 0
countB = 0
sumB = 0
for i in range(1, n + 1):
    if i % k == 0:
        countA += 1
        sumA += i
    else:
        countB += 1
        sumB += i
print('%.1f' % (sumA / countA), '%.1f' % (sumB / countB), sep=' ')
