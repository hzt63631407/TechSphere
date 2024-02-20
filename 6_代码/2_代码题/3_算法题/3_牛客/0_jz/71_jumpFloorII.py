

# 描述
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
# 求该青蛙跳上一个n级的台阶(n为正整数)总共有多少种跳法。

# 对于最后一级台阶，我们可以由倒数第二级台阶跳1步，也可以由倒数第三级太极跳两步，
# 即f(n)=f(n−1)+f(n−2)+...+f(n−(n−1))+f(n−n)=
# f(0)+f(1)+f(2)+...+f(n−1)f(n)=2∗f(n−1)

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