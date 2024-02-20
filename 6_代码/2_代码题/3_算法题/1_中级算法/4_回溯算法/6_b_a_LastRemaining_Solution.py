

# JZ62 孩子们的游戏(圆圈中最后剩下的数)
#
# 每年六一儿童节，牛客都会准备一些小礼物和小游戏去看望孤儿院的孩子们。
# 其中，有个游戏是这样的：首先，让 n 个小朋友们围成一个大圈，小朋友们的编号是0~n-1。
# 然后，随机指定一个数 m ，让编号为0的小朋友开始报数。
# 每次喊到 m-1 的那个小朋友要出列唱首歌，然后可以在礼品箱中任意的挑选礼物，并且不再回到圈中，
# 从他的下一个小朋友开始，继续0... m-1报数....这样下去....直到剩下最后一个小朋友，
# 可以不用表演，并且拿到牛客礼品，请你试着想下，哪个小朋友会得到这份礼品呢？
#
#
# step 1：首先判断没有小朋友的特殊情况。
# step 2：然后递归计算子问题，并将子问题的结果x运算(m+x)%n得到父级问题的结果。

import sys
sys.setrecursionlimit(100000)

class Solution:
    def LastRemaining_Solution(self, n: int, m: int) -> int:
        # write code here
        if n == 0 or m == 0:
            return -1
        return self.function(n, m)


    def function(self, n: int, m: int) -> int:
        if n == 1:
            return 0
        # 递归
        x = self.function(n - 1, m)
        # 返回最后删除的那个元素
        return (m + x) % n
