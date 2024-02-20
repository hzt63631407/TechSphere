# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 实现 strStr() 函数。
#
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
#
# 示例 1:
#
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 示例 2:
#
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 说明:
#
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
#
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

# 自己 以前 答案
def strStr(self, haystack: str, needle: str) -> int:
    for j in range(0, len(haystack)):
        if needle[0] == haystack[j]:
            if needle == haystack[j:j + len(needle)]:
                return j
    return -1


# 答案
# def strStr(self, haystack: str, needle: str) -> int:
#     return haystack.find(needle)

# h = "hello"
# n = ""
# print(strstr(h,n))



if __name__ == "__main__":
    print(str_str("hel1llo", "ll"))
    print(str_str("hel1lleo", "le"))

    # a = "hello"
    # b = "ll"
    # if b in a:
    #     print("t")
    #
    # a = [1, 2, 3, 4, 5, 6, 7, 8, 10]
    # b = [3, 4]
    # if b in a:
    #     print("s")




