
# 描述
# 给定两个字符串str1和str2,输出两个字符串的最长公共子串
# 题目保证str1和str2的最长公共子串存在且唯一。


def LCS(self , str1 , str2 ):
    a, b = '', ''
    for i in str1:
        a += i                          # 每次a都加1
        if a in str2:                   #
            b = a
        else:
            a = a[1:]                   # 每次循环都加1，如果不是就减1，保证新来校验是否在str2里的字符串至少和b一样长，
    return b                            # 即a的长度如果大的b，那么就更新b，如果没有大于b，先减1，再加1，会和b一样长



# 滑窗这样写可能更加直接一点吧， 1.首先给字符串1定义一个头指针，
# 然后比较str1[left,i]这个子字符串是否在串2中，
# 若在赋值给res 2.若不在，则将left+1，继续向后移动，直到结束

class Solution:
    def LCS(self , str1: str, str2: str) -> str:
        # write code here        res=""
        left=0
        for i in range(len(str1)+1):
            if str1[left:i+1] in str2:
                res=str1[left:i+1]
            else:
                left=left+1
        return res


