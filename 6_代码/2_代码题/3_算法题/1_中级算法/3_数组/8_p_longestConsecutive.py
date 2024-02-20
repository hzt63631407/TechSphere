
# leetcode 128
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
#
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
#
# https://leetcode.cn/problems/longest-consecutive-sequence/solution/zui-chang-lian-xu-xu-lie-by-leetcode-solution/


# 答案
def longestConsecutive(self, nums: List[int]) -> int:
    l = 0
    m = 0
    nums_set = set(nums)
    for num in nums_set:
        if num - 1 not in nums_set:
            l = 1
            while num + 1 in nums_set:
                l = l + 1
                num += 1
            m = max(m, l)
    return m

# 答案
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


# 有问题,只是每个小片段连续
def longestConsecutive(self, nums: List[int]) -> int:
    nums.sort()
    l = 1
    for i in range(0, len(nums) - 1):
        if nums[i + 1] == nums[i] + 1:
            l += 1
    return l