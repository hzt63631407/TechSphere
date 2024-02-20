# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# leetcode 125

# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:
#
# 输入: "race a car"
# 输出: false
import re

# 自己
# 想法：先讲字符串变成大/小写，然后除以2，用s[1] == s[-1] 方法进行判断


# 答案
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = filter(str.isalnum, s.lower())
    s = "".join(s)
    return s == s[::-1]

# 扩展
# str = "this2009";  # 字符中没有空格
# print str.isalnum();        只返回数字和字母  True
#
# str = "this is string example....wow!!!";
# print str.isalnum();          False

# filter(function, iterable)
# 参数
# function -- 判断函数。
# iterable -- 可迭代对象。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表中


# 自己 没有删除空格,：等。
def is_palindrom(a):
    al = a.lower()
    al1 = al[::-1]
    if al == al1:
        return True
    else:
        return False

print(is_palindrom("A man, a plan, a canal: Panama"))