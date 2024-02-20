

# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。
# 如果不存在 公共子序列 ，返回 0 。
#
# 输入：text1 = "abcde", text2 = "ace"
# 输出：3
# 解释：最长公共子序列是 "ace" ，它的长度为 3 。

# https://leetcode.cn/problems/qJnOS7/solution/zui-chang-gong-gong-zi-xu-lie-by-leetcod-ugg7/

# 定义 dp[i][j] 表示text1的前 i 个字符和text2的前 j 个字符之间最长 公共子序列 的长度
# 从问题的本质出发，对于两个给定的字符串，
# 我们容易发现 dp[i][j] 随着字符数目的增加（即 i 和 j 增大）是单调不减的，即有：

def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


