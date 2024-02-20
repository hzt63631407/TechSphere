
# leetcode724

# 给你一个整数数组 nums ，请计算数组的 中心下标 。
#
# 数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。

# 左求和*2+中心索引值 = 总和

def pivotIndex(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    s = sum(nums)
    t = 0
    for i in range(len(nums)):
        if t == s - nums[i] - t:
            return i
        else:
            t += nums[i]
    return -1
