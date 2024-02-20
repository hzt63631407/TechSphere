# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
#
# 示例：
#
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
# 说明：
#
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。

# def minWindow(self, s: str, t: str) -> str:
#     need, missing = collections.Counter(t), len(t)
#     i = start = end = 0
#     for j, c in enumerate(s, 1):
#         missing -= need[c] > 0
#         need[c] -= 1
#         if not missing:
#             while need[s[i]] < 0:
#                 need[s[i]] += 1
#                 i += 1
#             if not end or j - i < end - start:
#                 start, end = i, j
#     return s[start:end]


# 答案
# from collections import defaultdict
# class Solution(object):
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         mem = defaultdict(int)
#         for char in t:
#         	mem[char]+=1
#         t_len = len(t)
#         print(mem)
#         minLeft, minRight = 0,len(s)
#         left = 0
#
#         for right,char in enumerate(s):
#         	if mem[char]>0:
#         		t_len-=1
#         	mem[char]-=1
#
#         	if t_len==0:
#         		while mem[s[left]]<0:
#         			mem[s[left]]+=1
#         			left+=1
#
#         		if right-left<minRight-minLeft:
#         			minLeft,minRight = left,right
#
#         		mem[s[left]]+=1
#         		t_len+=1
#         		left+=1
#         return '' if minRight==len(s) else s[minLeft:minRight+1]



# 经典
# 自己 两个函数 把所有的都加了进去
# def i_in_t(t, s):
#     for i in t:
#         if i in s:
#             continue
#         else:
#             return False
#     return True


# def min_window(nums, t):
#     l = []
#     for i in range(0, len(nums) + 1):
#         for j in range(0, len(nums) + 1):
#             if i < j:
#                 s = nums[i:j]
#                 flag = i_in_t(t, s)
#                 if flag == True:
#                     l.append(s)
#
#     return l
#
#
# # 答案 滑动
# def minWindow(s, t):
#     ls = len(s)
#     lt = len(t)
#     if not s or not t or ls < lt:
#         return ''
#     min_size = ls + 1
#     l = r = 0
#     start = 0
#     end = ls - 1
#     map = {}
#     # 对t中的字符计数
#     for c in t:
#         map[c] = map.get(c, 0) + 1
#     match = 0
#     while r < ls:
#         map[s[r]] = map.get(s[r], 0) - 1
#         # 如果当前遇到的字符在map中出现过，则匹配数+1
#         match = match + 1 if map[s[r]] >= 0 else match
#         # 当匹配完成时窗口左滑
#         if match == lt:
#             # 尝试左滑窗口 对之前遇到的字符出窗口
#             while map[s[l]] < 0:
#                 map[s[l]] += 1
#                 l += 1
#             if min_size > r - l + 1:
#                 min_size = r - l + 1
#                 start = l
#                 end = r
#         r += 1
#     return '' if min_size > ls else s[start:end + 1]


if __name__ == "__main__":
    s = "dasfadas"
    t = "dsf"
    print(min_window(s, t))

    # min_window()
