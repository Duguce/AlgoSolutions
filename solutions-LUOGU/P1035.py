k = int(input())
i = 1
s = 1
isEnd = True
while isEnd:
    i += 1
    s += 1 / i
    if s > k:
        isEnd = False

print(i)
