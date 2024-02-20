# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个非空字符串s和一个包含非空单词列表的字典wordDict，判定s
# 是否可以被空格拆分为一个或多个在字典中出现的单词。

#
# 说明：
#
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 示例 2：
#
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
# 示例 3：
#
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false

# 此题目就是用背包中的dict 内容填满整个 字符串即可       如果dict填满了s 则满足


# 动态规划解题思路，找到转移方程 dp[i] = xx


# 动态规划，转移方程dp[i] = dp[j] and s[j, i-1]，此处需注意dp[i]、dp[j]表示的是从0到i-1、j-1，共i个、j个，而s[j,i-1]就是数组下标j到i-1，
# 比如示例1”leetcode“，dp[8] = dp[4] and s[4, 7]，dp[4]代表下标0~3的值"leet"是否在字典中，s[4,7]代表下标4~7的值"code"，
# 这样做是为了满足边界条件，即i=任意值时，s[j, i-1]可以取到i个全部数。比如”leetcode“，dp[8] = dp[0] and s[0, 7]，
# 其中s[0,7]为"leetcode"，dp[0]初始化为true（不代表任何组合，仅为边界条件），
# 如果写成dp[i] = dp[j] and s[j+1, i],dp[3] = dp[3] and s[4,7]，即dp的下标和s下标都是数组正常下标，
# 从第一个数到最后一个数就无法表示了，不能写为dp[0] = dp[0] and s[1,7],dp[0]表示了"l",s[1,7]表示了"eetcode"。




# 答案
# https://leetcode-cn.com/problems/word-break/solution/dong-tai-gui-hua-ji-yi-hua-hui-su-zhu-xing-jie-shi/
def wordBreak(s, wordDict):
    n = len(s)
    dp = [False]*(n+1)
    dp[0] = True
    for i in range(n):
        for j in range(i+1,n+1):
            if (dp[i] and (s[i:j] in wordDict)):
                dp[j] = True
        return dp[-1]


# 答案
# def wordBreak(s, wordDict):
#     dp = [False] * (len(s) + 1)
#
#     dp[0] = True
#
#     for i in range(1, len(s) + 1):  # 第一层循环是字符串
#
#         for word in wordDict:  # 循环每个dict，看是否能装进去
#             # print(i)
#             # print(len(word))
#             # if(s[i - len(word):i] == word):
#             # print("2:"+s[i - len(word):i])
#
#             if (i >= len(word) and s[i - len(word):i] == word):  # 这里注意，需要满足当前str[i-len(word):i]  的字符串正好等于dict中的字符串。
#
#                 # print("3:"+s[i - len(word):i])
#                 # print(dp[i - len(word)])                         #
#                 print(i)                                           # 通过i判断是否接上一个 如果不接 还是false 以后就一直false了
#                 dp[i] = dp[i] or dp[i - len(word)]  # 取一个能装进去的就是True
#
#     return dp, dp[-1]


if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code", "32"]
    # print(s[0:1])
    print(wordBreak(s, wordDict))
    # t = [0] * 4
    # print(t)
