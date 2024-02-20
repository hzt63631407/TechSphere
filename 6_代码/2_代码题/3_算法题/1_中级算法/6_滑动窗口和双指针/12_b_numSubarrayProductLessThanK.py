
# leecode 713. 乘积小于 K 的子数组
#
# 给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
#  
#
# 示例 1：
#
# 输入：nums = [10,5,2,6], k = 100
# 输出：8
# 解释：8 个乘积小于 100 的子数组分别为：
# [10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。


def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    """滑动具有单调性，所以滑窗"""
    left, res, curProduct = 0, 0, 1
    for right, num in enumerate(nums):
        curProduct *= num
        while left <= right and curProduct >= k:
            curProduct /= nums[left]
            left += 1
        res += right - left + 1
    return res