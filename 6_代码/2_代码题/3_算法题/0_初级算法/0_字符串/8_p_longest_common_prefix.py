# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# leecode 14

# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
#
# 所有输入只包含小写字母 a-z 。

# 自己
# 截取str[0][:i]与后面比较
def longestCommonPrefix(self, s: List[str]) -> str:
    s.sort(key=len)
    print(s)
    i = len(s[0])
    j = 0
    while i > 0 and j < len(s):
        while s[0][:i] != s[j][:i]:         # 要用while
            i -= 1
        j += 1
    return s[0][:i]



# 思路如下： 找出第一个串和第二个串的公共前缀s，然后找s和第三个串的公共前缀s2，依次进行到最后一个即可
# def longestCommonPrefix(self, strs):
#     strs.sort(key=len)
#     i = 0
#     if strs == []:
#         return ""
#     l = len(strs[0])
#     while i < len(strs):
#         if strs[i][:l] != strs[0][:l]:
#             l -= 1
#         i += 1
#     return strs[0][:l]

s = ["flower","flow","flight"]
d = ["dog","racecar","car"]
# s = ["flower","f","flight"]
print(longest_common_prefix(s))

# 判断长度
s=  ["flower","flow","flight"]
s = sorted(s,key=len)
print(s)


