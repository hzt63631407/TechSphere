# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

# 自己
# 思路 左边的括号数大于等于右边的括号数

# 结束条件 left = right = n


# 答案
def generate_parenthesis(n):
    reslut = []
    s = ""
    def backtrack(s,left,right):
        if left < n:
            backtrack(s+'(',left+1, right)
        if left > right:
            backtrack(s+')',left,right+1)
        if left == right == n:
            reslut.append(s)
    backtrack(s, 0, 0)
    return reslut





























# def generate_parenthesis(n):
#     res = []
#     def backtrace(s,left,right):
#         if left == n and right == n:
#             res.append(s)
#         if left < n:
#             backtrace(s + "(", left + 1, right)
#         if right < left:
#             backtrace(s + ")", left, right + 1)
#     backtrace("", 0, 0)
#     return res


if __name__ == "__main__":
    print(generate_parenthesis(4))



