
# 总结，如果提供了target不用相等，如果没有，那么就要相等


# 请实现无重复数字的升序数组的二分查找
#
# 给定一个 元素升序的、无重复数字的整型数组 nums 和一个目标值 target ，
# 写一个函数搜索 nums 中的 target，如果目标值存在返回下标（下标从 0 开始），否则返回 -1

# leetcode 704
# 有序用=，旋转不用
# 二分都是分治思想


def search(self , nums: List[int], target: int) -> int:
    # write code here
    left = 0
    right = len(nums ) -1
    if nums == []:
        return -1
    while left <= right:
        mid = (left +right ) // 2
        if nums[mid] > target:
            right = mid - 1
        if nums[mid] < target:
            left = mid + 1
        if nums[mid] == target:
            return mid
    return -1