################################################
# hint
# 本题是做数字反转的，我想到两种解法：
# 解法1：抛数位再补位，暴力循环
# 易错点：要考虑正负号！
################################################
n = int(input())  # 输入一个正整数n
y = 0  # 定义一个反转后的数字y
temp = n  # 设置一个中间数
if n < 0:
    temp = -n
    while temp != 0:
        y = y * 10 + temp % 10
        temp //= 10
    y = -y
else:
    while temp != 0:
        y = y * 10 + temp % 10
        temp //= 10
print(y)

################################################
# 解法2：字符串反转
# 易错点1：同样是要注意正负号问题
# 易错点2：删除反转后的数字最高位上的0，这个可以直接将y转为int类型
# python3可以直接对字符串类型进行遍历，实现反转方便很多
# 当然，也可以自己将变量类型转为字符串，然后通过循环反转
################################################
n = int(input())  # 输入一个正整数n
y = 0  # 定义一个反转后的数字y
temp = n  # 设置一个中间数
if temp < 0:
    temp = -temp
    y = str(temp)[::-1]
    print(-int(y))
else:
    y = str(temp)[::-1]
    print(int(y))
