
# 给定一个含有 n 个正整数的数组和一个正整数 target 。
#
# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 
# [numsl, numsl+1, ..., numsr-1, numsr] ，
# 并返回其长度。如果不存在符合条件的子数组，返回 0 。
#
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。

# 一般求子串，用到互动窗口，双指针

def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    ans = n + 1
    start, end = 0, 0
    total = 0
    while end < n:
        total += nums[end]
        while total >= s:
            ans = min(ans, end - start + 1)
            total -= nums[start]
            start += 1
        end += 1
    if ans == n + 1:
        return 0
    else:
        return ans

