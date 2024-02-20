
# 451. 根据字符出现频率排序
#
# 给定一个字符串 s ，根据字符出现的 频率 对其进行 降序排序 。一个字符出现的 频率 是它出现在字符串中的次数。
#
# 返回 已排序的字符串 。如果有多个答案，返回其中任何一个。
#
# 示例 1:
#
# 输入: s = "tree"
# 输出: "eert"
# 解释: 'e'出现两次，'r'和't'都只出现一次。
# 因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。


def frequencySort(self, nums: str) -> str:
    d = {}
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = 1
        else:
            d[nums[i]] += 1
    a = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print(a)
    b = ""
    for i in range(len(a)):
        b += a[i][0] * int(a[i][1])
    return b