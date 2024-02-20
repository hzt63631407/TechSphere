

# NC165 最长公共子序列(一)
#
# 描述
# 给定两个字符串 s1 和 s2，长度为m和n 。求两个字符串最长公共子序列的长度。
# 所谓子序列，指一个字符串删掉部分字符（也可以不删）形成的字符串。
# 例如：字符串 "arcaea" 的子序列有 "ara" 、 "rcaa" 等。但 "car" 、 "aaae" 则不是它的子序列。
# 所谓 s1 和 s2 的最长公共子序列，即一个最长的字符串，它既是 s1 的子序列，也是 s2 的子序列。
# 数据范围 : 0\leq m,n\leq 10000≤m,n≤1000 。保证字符串中的字符只有小写字母。

class Solution:
    def LCS(self , s1: str, s2: str) -> int:
        # write code here
        dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i -1][j], dp[i][j - 1])
        return dp[-1][-1]