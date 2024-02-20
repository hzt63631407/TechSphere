# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
#
#
# 示例 1：
#
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"

# 答案
# def longestValidParentheses(self, s: str) -> int:
#     if not s:
#         return 0
#     res = []
#     stack = []
#     for i in range(len(s)):
#         if stack and s[i] == ")":
#             res.append(stack.pop())
#             res.append(i)
#         if s[i] == "(":
#             stack.append(i)
#     res.sort()
#     #print(res)
#     i = 0
#     ans = 0
#     n = len(res)
#     while i < n:
#         j = i
#         while j < n - 1 and res[j + 1] == res[j] + 1:
#             j += 1
#         ans = max(ans, j - i + 1)
#         i = j + 1
#     return ans

