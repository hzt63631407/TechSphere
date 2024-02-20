
# leecode 30
# 给定一个字符串 s 和一些 长度相同 的单词 words 。
# 找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

# 输入：s = "barfoothefoobarman", words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。

def findSubstring(s: str, words: List[str]) -> List[int]:
    if not s or not words: return []
    one_word = len(words[0])
    all_len = len(words) * one_word
    n = len(s)
    words = Counter(words)
    res = []
    for i in range(0, n - all_len + 1):
        tmp = s[i:i + all_len]
        c_tmp = []
        for j in range(0, all_len, one_word):
            c_tmp.append(tmp[j:j + one_word])
        if Counter(c_tmp) == words:
            res.append(i)
    return res

