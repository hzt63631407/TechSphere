# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# leetcode 334 递增的三元子序列
# 给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。
#
# 数学表达式如下:
#
# 如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
# 使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。
#
# 示例 1:
#
# 输入: [1,2,3,4,5]
# 输出: true
# 示例 2:
#
# 输入: [5,4,3,2,1]
# 输出: false

# 答案
# 循环遍历数组，
# a 始终记录最小元素，b 为某个子序列里第二大的数。
# 接下来不断更新 a，同时保持 b 尽可能的小。
# 如果下一个元素比 b 大，说明找到了三元组

# 自己
def increaing_triplet(nums):
    length = len(nums)
    if length < 3:
        return False
    min_num = float('inf')          # float('inf')  表示正无穷，float('-inf')表示负无穷
    max_num = float('inf')
    for n in nums:
        if n < min_num:
            min_num = n
        elif min_num < n and n <= max_num:
            max_num = n
        elif n > max_num:
            return True
    return False

# 自己 以前
# def increaing_triplet(nums):
#     length = len(nums)
#     if length < 3:
#         return False
#     min_num = float('inf')
#     max_num = float('inf')
#     for n in nums:
#         n = int(n)
#         if n < min_num:
#             min_num = n
#             print(min_num)
#         elif min_num < n and n <= max_num:
#             max_num = n
#             print(max_num)
#         elif n > max_num:
#             return True
#
#     return False




if __name__ == "__main__":
    a = "32125"
    print(increaing_triplet(a))
