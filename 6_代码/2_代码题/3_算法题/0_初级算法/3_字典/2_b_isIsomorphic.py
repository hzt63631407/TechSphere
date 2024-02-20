
# leetcode 205. 同构字符串

# 给定两个字符串 s 和 t ，判断它们是否是同构的。
# 如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，
# 相同字符只能映射到同一个字符上，字符可以映射到自己本身。

# 输入：s = "egg", t = "add"
# 输出：true

# 因此，我们维护两张哈希表，第一张哈希表 \textit{s2t}s2t 以 ss 中字符为键，
# 映射至 tt 的字符为值，第二张哈希表 \textit{t2s}t2s 以 tt 中字符为键，映射至 ss 的字符为值。
# 从左至右遍历两个字符串的字符，不断更新两张哈希表，
# 如果出现冲突（即当前下标 \textit{index}index 对应的字符 s[\textit{index}]s[index]
# 已经存在映射且不为 t[\textit{index}]t[index] 或当前下标 \textit{index}index 对应的字符
# t[\textit{index}]t[index] 已经存在映射且不为 s[\textit{index}]s[index]）
# 时说明两个字符串无法构成同构，返回 \rm falsefalse。

def isIsomorphic(self, s: str, t: str) -> bool:
    if len(t) != len(s):
        return False
    s2t = {}
    t2s = {}
    for i in range(len(s)):
        s_c, t_c = s[i], t[i]
        if s_c not in s2t:
            s2t[s_c] = t_c
        if t_c not in t2s:
            t2s[t_c] = s_c
        if s2t[s_c] != t_c or t2s[t_c] != s_c:
            return False
    return True


def isIsomorphic(self, s: str, t: str) -> bool:
    sd = {}
    td = {}
    for i in range(len(s)):
        if s[i] not in sd:
            sd[s[i]] = t[i]
        if t[i] not in td:
            td[t[i]] = s[i]
        if s[i] in sd or t[i] in td:
            if sd[s[i]] != t[i] or td[t[i]] != s[i]:
                return False
    return True