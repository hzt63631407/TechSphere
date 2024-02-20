# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 反转一个字符串的"s"中的元音字母。
# 输入 "leetcode" 输出"leotcede"

def reverse(s):
    a = "aeiou"
    l = []
    ans = ""
    count = 0
    for i in range(len(s)):
        if s[i] in a:
            l.append(s[i])
    l.reverse()
    for i in range(len(s)):
        if s[i] not in l:
            ans += s[i]
        if s[i] in l:
            ans += l[count]
            count += 1
    return ans
print(reverse("apple"))
print(reverse("leetcode"))


def reverse(s):
    a = "aeoiu"
    dic = {}
    count = 0
    ans = ""
    for i in range(len(s)):
        if s[i] in a:
            count += 1
            dic[count] = s[i]
    for i in range(len(s)):
        if s[i] not in a:
            ans += s[i]
        if s[i] in a:
            ans += dic[count]
            count -= 1
    return ans


print(reverse("leetcode"))







