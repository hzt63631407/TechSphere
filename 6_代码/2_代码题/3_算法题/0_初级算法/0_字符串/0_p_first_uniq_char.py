# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#
# 案例:
#
# s = "leetcode"
# 返回 0.
#
# s = "loveleetcode",
# 返回 2.


# 答案

def firstUniqChar(s):
    for i in range(len(s)):
        if s[i] not in s[:i] and s[i] not in s[i+1:]:
            return s[i]
    return -1


if __name__ == "__main__":
    a = "eedtcodet"
    answer = firstUniqChar(a)
    print(answer)