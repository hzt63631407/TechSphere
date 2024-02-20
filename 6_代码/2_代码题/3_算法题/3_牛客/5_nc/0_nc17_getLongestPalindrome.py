

# 描述
# 对于长度为n的一个字符串A（仅包含数字，大小写英文字母），
# 请设计一个高效算法，计算其中最长回文子串的长度。


# 没有超出时间复杂度
class Solution:
    def getLongestPalindrome(self , a: str) -> int:
        # write code here
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
            return len(l2[-1])