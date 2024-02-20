

# leetcode 49

# 给你一个字符串数组，请你将 字母异位词 组合在一起。
# 可以按任意顺序返回结果列表。
#
# 字母异位词 是由重新排列源单词的字母得到的一个新单词，
# 所有源单词中的字母通常恰好只用一次。

# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    dic = {}
    for s in strs:
        keys = "".join(sorted(s))
        print(keys)
        if keys not in dic:
            dic[keys] = [s]
        else:
            dic[keys].append(s)                 # key对应的value可以改变
    return list(dic.values())
    # l = sorted(dic.values())
    # return l