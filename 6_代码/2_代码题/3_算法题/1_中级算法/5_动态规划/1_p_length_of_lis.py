# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 300. 最长递增子序列
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例:
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 说明:
#
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n2) 。
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?


# 子序列的问题->动态规划。
#
# 使用数组 cell 保存每步子问题的最优解。
# cell[i] 代表含第 i 个元素的最长上升子序列的长度。
# 求解 cell[i] 时，向前遍历找出比 i 元素小的元素 j，令 cell[i] 为 max（cell[i],cell[j]+1)

## 注意 dp方程不能进行累加，应该和前面所有的比，找出最多的，如果自身大，就累加

# 自己
# nums = [10, 9, 2, 5, 1, 101, 3, 18]

# 答案
# def length_of_lis(nums):
#     if nums == []:
#         return 0
#     cell = [1] * len(nums)
#     for i in range(1, len(nums)):
#         for j in range(i):
#             if (nums[j] < nums[i]):
#                 cell[i] = max(cell[i], cell[j] + 1)
#     return max(cell)


# 答案 写的不好
# def length_of_lis(nums):
#     if nums == []:
#         return 0
#     dp = [0 * len(nums)]
#     for i in range(1, len(nums)):
#         for j in range(i):
#             if (nums[j] < nums[i]):                         # 如果比之前的某个元素大，在原来的某个元素上+1，
#                 cell[i] = max(cell[i], cell[j] + 1)
#     return max(cell)


if __name__ == "__main__":
    # nums = [10, 9, 2, 5, 3, 7, 101, 18]
    nums = [10, 9, 2, 5, 1, 3, 2, 18]
    print(length_of_lis(nums))
