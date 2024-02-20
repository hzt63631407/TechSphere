# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。
#
# 返回所有可能的结果。答案可以按 任意顺序 返回。
#
#  
#
# 示例 1：
#
# 输入：s = "()())()"
# 输出：["(())()","()()()"]
#
# https://leetcode-cn.com/problems/remove-invalid-parentheses/solution/shan-chu-wu-xiao-de-gua-hao-by-leetcode-9w8au/

# 答案
# class Solution:
#     def removeInvalidParentheses(self, s: str) -> List[str]:
#         def isValid(s):
#             count = 0
#             for c in s:
#                 if c == '(':
#                     count += 1
#                 elif c == ')':
#                     count -= 1
#                     if count < 0:
#                         return False
#             return count == 0
#
#         ans = []
#         currSet = set([s])
#
#         while True:
#             for ss in currSet:
#                 if isValid(ss):
#                     ans.append(ss)
#             if len(ans) > 0:
#                 return ans
#             nextSet = set()
#             for ss in currSet:
#                 for i in range(len(ss)):
#                     if i > 0 and ss[i] == s[i - 1]:
#                         continue
#                     if ss[i] == '(' or ss[i] == ')':
#                         nextSet.add(ss[:i] + ss[i + 1:])
#             currSet = nextSet
#         return ans

