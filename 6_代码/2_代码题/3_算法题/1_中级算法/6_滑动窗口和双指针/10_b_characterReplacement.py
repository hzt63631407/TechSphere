

# 424. 替换后的最长重复字符
#
# 给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。
# 该操作最多可执行 k 次。
#
# 在执行上述操作后，返回包含相同字母的最长子字符串的长度。
#
# 示例 1：
#
# 输入：s = "ABAB", k = 2
# 输出：4
# 解释：用两个'A'替换为两个'B',反之亦然。


# 这里采用滑动窗口，当滑动窗口达到一个最大值后，窗口一直前进
# 当窗口内记载的出现次数最大字符大于上一次的出现最大次数字符时，窗口长度增加
# 否则，窗口保持原来长度前进一个单位
from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res, m, maxl = 0, collections.Counter(), 0
        for i in range(len(s)):
            m[s[i]] += 1
            maxl = max(maxl, m[s[i]])
            if res - maxl < k:
                res += 1
            else:
                m[s[i - res]] -= 1
        return res


