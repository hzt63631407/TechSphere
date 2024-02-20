
# leetcode 290

# 给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。
#
# 这里的 遵循 指完全匹配，
# 例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。
#
#
# 示例1:
#
# 输入: pattern = "abba", s = "dog cat cat dog"
# 输出: true

def wordPattern(self, pattern: str, s: str) -> bool:
    s = s.split()
    if len(s) != len(pattern):
        return False
    p_d = {}
    s_d = {}
    for i in range(len(s)):
        s_i = s[i]
        p_i = pattern[i]
        if s_i not in s_d:
            s_d[s_i] = pattern[i]
        if p_i not in p_d:
            p_d[p_i] = s[i]
        if s_d[s_i] != pattern[i] or p_d[p_i] != s[i]:
            return False
    return True