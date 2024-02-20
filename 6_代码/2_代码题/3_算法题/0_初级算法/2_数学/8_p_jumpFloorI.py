
# 描述
#
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。
# 求该青蛙跳上一个 n 级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

class Solution:
    def jumpFloor(self , number: int) -> int:
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2
        f1 = 1
        f2 = 2
        for i in range(3,number+1):
            fn = f1 + f2
            f1 = f2
            f2 = fn
        return fn

# 描述
#
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
# 求该青蛙跳上一个n级的台阶(n为正整数)总共有多少种跳法。

class Solution:
    def jumpFloorII(self , number: int) -> int:
        # write code here
        dp = [0 for i in range(number + 1)]
        #初始化前面两个
        dp[0] = 1
        dp[1] = 1
        #依次乘2
        for i in range(2, number + 1):
            dp[i] = 2 * dp[i - 1]
        return dp[number]