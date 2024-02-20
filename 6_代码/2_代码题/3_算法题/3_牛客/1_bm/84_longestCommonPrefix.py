
# 描述
# 给你一个大小为 n 的字符串数组 strs ，
# 其中包含n个字符串 , 编写一个函数来查找字符串数组中的最长公共前缀，返回这个公共前缀。

# 思路如下： 找出第一个串和第二个串的公共前缀s，然后找s和第三个串的公共前缀s2，依次进行到最后一个即可

class Solution:
    def longestCommonPrefix(self , strs: List[str]) -> str:
        # write code here
        strs.sort(key=len)
        i = 1
        if strs == []:
            return ""
        while i < len(strs):
            if strs[0] != strs[i][:len(strs[0])]:
                strs[0] = strs[0][:len(strs[0])-1]
            i += 1
        return strs[0]


# 自己    有点问题
# 取第一个字符串的各个字母和后面每个字符串进行判断
# def longest_common_prefix(list):
#     list = sorted(list, key=len)
#     for i in range(0,len(list[0])):
#         for k in range(1,len(list)):
#             if list[0][i] == list[k][i]:
#                 continue
#             else:
#                 if i == 0 :
#                     return -1
#                 print(i)
#                 return list[0][0:i]
#     return -1