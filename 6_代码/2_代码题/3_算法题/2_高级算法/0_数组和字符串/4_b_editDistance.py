

# BM75 编辑距离(一)
# 描述
# 给定两个字符串 str1 和 str2 ，请你算出将 str1 转为 str2 的最少操作数。
# 你可以对字符串进行3种操作：
# 1.插入一个字符
# 2.删除一个字符
# 3.修改一个字符。
#
#
# 输入：
# "nowcoder","new"
# 返回值：
# 6
# 复制
# 说明：
# "nowcoder"=>"newcoder"(将'o'替换为'e')，修改操作1次
# "nowcoder"=>"new"(删除"coder")，删除操作5次

# 用dp[i][j]表示从两个字符串首部各自到str1[i]和str2[j]为止的子串需要的编辑距离，
# 那很明显dp[str1.length][str2.length]就是我们要求的编辑距离。
#
# 如果遍历到str1[i]和 str2[j]的位置，这两个字符相同，
# 这多出来的字符就不用操作，操作次数与两个子串的前一个相同，
# 因此有dp[i][j]=dp[i−1][j−1]dp[i][j] = dp[i - 1][j - 1]dp[i][j]=dp[i−1][j−1]；
# 如果这两个字符不相同，那么这两个字符需要编辑，但是此时的最短的距离不一定是修改这最后一位，
# 也有可能是删除某个字符或者增加某个字符，因此我们选取这三种情况的最小值增加一个编辑距离，
# 即dp[i][j]=min(dp[i−1][j−1],min(dp[i−1][j],dp[i][j−1]))+1。


class Solution:
    def editDistance(self , str1: str, str2: str) -> int:
        n1 = len(str1)
        n2 = len(str2)
        #dp[i][j]表示到str1[i]和str2[j]为止的子串需要的编辑距离
        dp = [[0] * (n2 + 1) for i in range(n1 + 1)]
        #初始化边界
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, n2 + 1):
            dp[0][i] = dp[0][i - 1] + 1
        #遍历第一个字符串的每个位置
        for i in range(1, n1 + 1):
            #对应第二个字符串每个位置
            for j in range(1, n2 + 1):
                #若是字符相同，此处不用编辑
                if str1[i - 1] == str2[j - 1]:
                    #直接等于二者前一个的距离
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    #选取最小的距离加上此处编辑距离1
                    dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1
        return dp[n1][n2]
