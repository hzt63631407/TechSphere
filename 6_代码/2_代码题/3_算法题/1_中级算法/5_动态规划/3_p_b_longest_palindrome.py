# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# leetcode 5
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"


# 自己 答案 太暴力 超出时间限制
def long_palindromea(a):
    l1 = []
    l2 = []

    for i in range(0, len(a)):                   # 找出所有的字段   整理出对应的代码
        for j in range(0,len(a)+1):
            if i < j :
                l = a[i:j]
                l1.append(l)
    max = 1
    for i in l1:                                 # 判断是不是回文字符串
        j = i[::-1]                              # 将列表反转
        if i == j:
            if len(i) >= max:                     # 获取列表中最长的元素的长度
                max = len(i)
                l2.append(i)
    return l2[-1]


# 答案
def longestPalindrome(self, s: str) -> str:
    n = len(s)
    if n < 2:
        return s
    max_len = 1
    begin = 0
    # dp[i][j] 表示 s[i..j] 是否是回文串
    dp = [[False] * n for i in range(n)]
    # dp = [[False] * n] * n        # 不行
    for i in range(n):
        dp[i][i] = True

    # 递推开始
    # 先枚举子串长度
    for L in range(2, n + 1):
        # 枚举左边界，左边界的上限设置可以宽松一些
        for i in range(n):
            # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
            j = L + i - 1
            # 如果右边界越界，就可以退出当前循环
            if j >= n:
                break

            if s[i] != s[j]:
                dp[i][j] = False
            else:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]  # 只有dp[0][4]是True,dp[1][3]还是True……,这才是真正的回文串
                    # dp[i][j] = True #假如s="abaa",s[0]=s[4], d[0][4]=True,就被认为是回文串，跳入下一个环节
            # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
            if dp[i][j] and j - i + 1 > max_len:
                max_len = j - i + 1
                begin = i
    return s[begin:begin + max_len]



# 给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。
# # 情况一：下标i 与 j相同，同一个字符例如a，当然是回文子串
# # 情况二：下标i 与 j相差为1，例如aa，也是文子串
# # 情况三：下标：i 与 j相差大于1的时候，例如cabac，
# # 此时s[i]与s[j]已经相同了，我们看i到j区间是不是回文子串就看aba是不是回文就可以了，
# # 那么aba的区间就是 i+1 与 j-1区间，这个区间是不是回文就看dp[i + 1][j - 1]是否为true。
#
# # dp[i][j]表示 i 到 j 的字符串能不能构成回文串,那么dp[i][j] = dp[i +1][j - 1] && (s[i] == s[j])
# # 评论
# def countSubstrings(self, s: str) -> int:
#     dp = [[False] * len(s) for _ in range(len(s))]
#     result = 0
#     for i in range(len(s) - 1, -1, -1):  # 注意遍历顺序
#         for j in range(i, len(s)):
#             if s[i] == s[j]:
#                 if j - i <= 1:  # 情况一 和 情况二
#                     result += 1
#                     dp[i][j] = True
#                 elif dp[i + 1][j - 1]:  # 情况三
#                     result += 1
#                     dp[i][j] = True
#     return result


print(long_palindromea('11213'))




































#
# def longest_palindromea(a):
#     l1 = []
#     l2 = []
#     l3 = []
#     for i in range(0, len(a)):
#         for j in range(0, len(a)):
#             if i <= j:
#                 l1 = a[i:j]
#                 for k in range(0, len(l1) / 2):
#                     if l1[k] == l1[-(k + 1)]:
#                         l2.append(l1)
#                         break
#                     else:
#                         break
#     # for i in l2:
#     #     if len(i) > len(l3):
#     #         l3 = i
#     return l2
#
#
# if __name__ == "__main__":
#     a = "bababd"
#     print(longest_palindromea(a))
