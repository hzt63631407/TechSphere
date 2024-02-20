

# leetcode 459. 重复的子字符串
#
# 给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。
#
# 示例 1:
#
# 输入: s = "abab"
# 输出: true
# 解释: 可由子串 "ab" 重复两次构成。

# 自己
def repeatedSubstringPattern(self, s: str) -> bool:
    i = 1
    while i < len(s):
        if (s[:i] * (len(s) // i)) == s:
            return True
        i += 1
    return False



def repeatedSubstringPattern(self, s: str) -> bool:
    for j in range(1, len(s)):
        if (s[:j]) * (len(s) // j) == s:
            return True
    return False