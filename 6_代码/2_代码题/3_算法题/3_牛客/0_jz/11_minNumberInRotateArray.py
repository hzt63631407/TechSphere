
# 描述
# 有一个长度为 n 的非降序数组，比如[1,2,3,4,5]，将它进行旋转，即把一个数组最开始的若干个元素搬到数组的末尾，
# 变成一个旋转数组，比如变成了[3,4,5,1,2]，或者[4,5,1,2,3]这样的。
# 请问，给定这样一个旋转数组，求数组中的最小值。


class Solution:
    def minNumberInRotateArray(self, nums):
        # write code here
        # 特殊情况判断
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r = r - 1
        return nums[l]