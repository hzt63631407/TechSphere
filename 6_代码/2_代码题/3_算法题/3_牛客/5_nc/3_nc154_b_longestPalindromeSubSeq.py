# 描述
# 给定一个字符串，找到其中最长的回文子序列，并返回该序列的长度。
#
# 注：回文序列是指这个序列无论从左读还是从右读都是一样的。
# 本题中子序列字符串任意位置删除k（len(s)>=k>=0）个字符后留下的子串。
#
# 输入："abccsb"
#
# 返回值：4
#
# 说明：
# 分别选取第2、3、4、6位上的字符组成“bccb”子序列是最优解

# 解题思路：
# 动态规划算法，
# dp[i][j]定义为：字符串从i到j是含有回文子序列的长度
#
# 1、当 i= =j时，dp[i][j ]= =1
# 2、当 j - i< =
# 2时，如s[i ]= =s[j]，dp[i][j] = j- i + 1
# 3、当j - i > 2
# 时, 如s[i] == s[j]，dp[i][j] = dp[i + 1][j - 1] + 2
# 4、如s[i] != s[j]
# 时，dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
#
# 由于递推公式：
# dp[i][j] = dp[i + 1][j - 1] + 2，i要从大的数值，j要从小的数值开始计算
# -*- coding:utf-8 -*-

class Solution:
    def longestPalindromeSubSeq(self, A, n):
        # write code here
        #print(A)
        #print(n)
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if A[i]==A[j]:
                    if j-i<=2:
                        dp[i][j] = j-i+1
                    else:
                        dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        #for i in dp:
        #    print(i)
        return dp[0][-1]

A = 'abccsb'   # 4
n = len(A)
s = Solution()
print(s.longestPalindromeSubSeq(A,n))