



# 输入一个长度为n的整型数组array，数组中的一个或连续多个整数组成一个子数组，
# 子数组最小长度为1。求所有子数组的和的最大值。

class Solution:
    def FindGreatestSumOfSubArray(self , nums: List[int]) -> int:
        # write code here
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i - 1], 0)
        return max(nums)
