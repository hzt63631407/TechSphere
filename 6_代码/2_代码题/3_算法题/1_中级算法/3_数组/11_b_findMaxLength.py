
# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，
# 并返回该子数组的长度。


# leetcode 剑值offer11

# class Solution:
def findMaxLength(nums: list[int]) -> int:##转化为和为0的最大连续数组
    d = {0: -1}         # 设定为-1 是因为相减之后数量需要加1 如8-4 但是数量是5
    ans = 0
    cur = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            cur += -1
        else:
            cur += 1
        if cur in d:
            if i - d[cur] > ans:
                ans = i - d[cur]
        else:
            d[cur] = i
    return ans

