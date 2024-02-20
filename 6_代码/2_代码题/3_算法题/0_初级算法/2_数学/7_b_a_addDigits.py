
# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。
#
# 输入: num = 38
# 输出: 2
# 解释: 各位相加的过程为：
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# 由于 2 是一位数，所以返回 2。

def addDigits(self, num: int) -> int:
    while num >= 10:
        sum = 0
        while num:
            sum += num % 10
            num //= 10
        num = sum
    return num
