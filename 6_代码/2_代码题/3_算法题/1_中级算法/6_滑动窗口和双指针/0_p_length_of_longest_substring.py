# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# leetcode 3
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


# 自己 答案
# def lengthOfLongestSubstring(self, s: str) -> int:
#     a = []
#     l = 0
#     for i in range(len(nums)):
#         while nums[i] in a:
#             a.remove(a[0])
#         a.append(nums[i])
#         if len(a) > l:
#             l = len(a)
#     return l


# 这道题主要用到思路是：滑动窗口
# 什么是滑动窗口？
# 其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，
# 当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！
# 如何移动？
# 我们只要把队列的左边的元素移出就行了，直到满足题目要求！
# 一直维持这样的队列，找出队列出现最长的长度时候，求出解！
def lengthOfLongestSubstring(self, s: str) -> int:
    if not s:
        return 0
    left = 0
    lookup = []
    n = len(s)
    max_len = 0
    cur_len = 0
    for i in range(n):
        cur_len += 1
        while s[i] in lookup:                               # 如果前面有，要移除，但不确定是第几个，所以要用while一直判断
            lookup.remove(s[left])
            left += 1
            cur_len -= 1
        if cur_len > max_len:
            max_len = cur_len
        lookup.append(s[i])
    return max_len






def lengthOfLongestSubstring(self, s: str) -> int:
    # write code here
    # 滑动窗口 + 哈希表
    mp = {}
    res = 0
    # 设置窗口左边界
    left = 0
    for right in range(len(s)):
        if s[right] in mp:
            mp[s[right]] += 1
        else:
            mp[s[right]] = 1
        # 窗口中有重复
        while mp[s[right]] > 1:
            mp[s[left]] -= 1
            left += 1
        # 维护子串长度最大值
        res = max(res, right - left + 1)
    return res



# 自己 求长度 有问题 不是答案
# def length_of_longest_substring(a):
#     l = []
#     max = 0
#     for i in a:
#         if i not in l:
#             l.append(i)
#         else:
#             if max < len(l):
#                 max = len(l)
#                 l = []
#                 l.append(i)                     # 重新开始计算时，要加上上次去掉的那一个，因为它不重复
#     return max



# 自己 以前
# def length_of_longest_substring(a):
#     l = []
#     len1 = 0
#     for i in range(0, len(a)):
#         for j in range(0, len(a)):
#             if i <= j:
#                 if a[j] not in l:
#                     l.append(a[j])
#                     # print(l)
#                 else:
#                     if len(l) > len1:
#                         len1 = len(l)
#                     del l[:]
#                     break
#     return len1
#
# def del_1(a):
#     print(a)
#     del a[:]
#     print(a)


if __name__ == "__main__":
    b1 = "123345121"
    b2 = "pwwkew"
    a1 = list(b1)
    a2 = list(b2)
    print(length_of_longest_substring(a1))
    print(length_of_longest_substring(a2))

    # print(del_1(a))
