
# 描述
# 给定一个长度为n的数组nums，请你找到峰值并返回其索引。
# 数组可能包含多个峰值，在这种情况下，返回任何一个所在位置即可。
# 1.峰值元素是指其值严格大于左右相邻值的元素。严格大于即不能有等于
# 2.假设 nums[-1] = nums[n] = −∞
# 3.对于所有有效的 i 都有 nums[i] != nums[i + 1]
# 4.你可以使用O(logN)的时间复杂度实现此问题吗？


# 代码正确，但是牛客提交时有问题
# 以后不需要做了
def findPeakElement(self , nums: List[int]) -> int:
    # write code here
    left = 0
    right = len(nums) - 1
    # 二分法
    while left < right:
        mid = int((left + right) / 2)
        # 右边是往下，不一定有坡峰
        if nums[mid] > nums[mid +1]:
            right = mid
        # 右边是往上，一定能找到波峰
        else:
            left = mid + 1
    # 其中一个波峰
    return right