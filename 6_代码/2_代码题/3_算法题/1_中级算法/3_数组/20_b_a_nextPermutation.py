# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。
#
# 例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
# 整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。
# 更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。
# 如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
#
# 例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
# 类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
# 而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
# 给你一个整数数组 nums ，找出 nums 的下一个排列。
#
# 必须 原地 修改，只允许使用额外常数空间。
# https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/

# 答案
def nextPermutation(self, nums: list) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) <= 1: return

    i, j, k = len(nums) - 2, len(nums) - 1, len(nums) - 1

    # find: A[i] < A[j]
    while i >= 0 and nums[i] >= nums[j]:
        i = i - 1
        j = j - 1

    if i >= 0:  # 不是最后一个排列
        # find: A[i] < A[k]
        while nums[i] >= nums[k]:
            k = k - 1
        # swap A[i], A[k]
        nums[i], nums[k] = nums[k], nums[i]

    # reverse A[j:end]
    end = len(nums) - 1
    while j < end:
        nums[j], nums[end] = nums[end], nums[j]
        j = j + 1
        end = end - 1