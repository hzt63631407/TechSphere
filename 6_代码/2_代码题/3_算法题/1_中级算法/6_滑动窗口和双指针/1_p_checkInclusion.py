
# 567. 字符串的排列
# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。
# 如果是，返回 true ；否则，返回 false 。
#
# 换句话说，s1 的排列之一是 s2 的 子串 。
#
#  
#
# 示例 1：
#
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
#
# 答案
#
# 将s1的Counter对象和s2中长度相同的连续字符的Counter对象进行比较，出现相等返回True。

from collections import Counter
def checkInclusion(self, s1: str, s2: str) -> bool:
    s1_map = Counter(s1)
    i = 0
    while i+ len(s1) <= len(s2):
        target_map = Counter(s2[i: i + len(s1)])
        if target_map == s1_map:
            return True
        i += 1
    return False