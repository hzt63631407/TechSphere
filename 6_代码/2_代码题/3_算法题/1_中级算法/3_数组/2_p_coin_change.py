# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
#
# 示例 1:
#
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1
# 示例 2:
#
# 输入: coins = [2], amount = 3
# 输出: -1
# 说明:
# 你可以认为每种硬币的数量是无限的。


# 以前答案 答案正确
# 对硬币进行倒叙，
def coin_change(coins, amout):
    a = []
    for i in range(len(coins), 0, -1):
        temp1 = amout // coins[i - 1]                   # //不取余    / 取余
        temp2 = amout % coins[i - 1]                    #
        amout = temp2
        a.append(temp1)
        if temp2 == 0:
            return len(a)
    return -1


# “/”，这是传统的除法，3/2=1.5
# “//”，在python中，这个叫“地板除”，3//2=1
# “%”，这个是取模操作，也就是区余数，4%2=0，5%2=1

# 排序 不断取余
# 自己 解题思路不对，用以前答案
# def coin_change(coins, amout):
#     a = sorted(coins)
#     temp = []
#     count = 0
#     for i in range(0, len(a)):
#         temp[i] = amout // a[-(i+1)]
#         amout = temp[i]
#         count = count + amout
#         temp[i] = amout % a[-(i+1)]
#         amout = temp[i]
#         count = count + amout
#         if amout == 0 :
#             return count
#     return -1

if __name__ == "__main__":
    coins = [1,2,5]
    amout = 11
    print(coin_change(coins, amout))

