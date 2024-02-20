# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，
# 那么整个数组都会变为升序排序。
#
# 请你找出符合题意的 最短 子数组，并输出它的长度。
#
# 示例 1：
#
# 输入：nums = [2,6,4,8,10,9,15]
# 输出：5
# 解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
#
# 示例 2：
#
# 输入：nums = [1,2,3,4]
# 输出：0

# 答案
# 使用排序，然后将排序后的数组与排序前对比，找到最开始和最后元素不同的位置
def findUnsortedSubarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left, right = 0, -1
    new_nums = sorted(nums)
    for i in range(len(nums)):
        if nums[i] != new_nums[i]:
            left = i
            break
    for i in range(len(nums)):
        if nums[i] != new_nums[i]:              # 没有break 所以能找到最后不同的位置
            right = i
    return right - left + 1


# 自己 思路正确 但超时了
# def find_unsorted_subarray(list):
#     count = 0
#     k = len(list)
#     while len(list) != 0:
#         if list[0] == min(list):
#             count = count + 1
#             del list[0]
#     while len(list) != 0:
#         if list[-1] == max(list):
#             count = count + 1
#             del list[-1]
#     return k  - count


list = [1,2,3,2,5,6,8,10,9,15]
# list = [1,2,3,4]
print(findUnsortedSubarray(list))