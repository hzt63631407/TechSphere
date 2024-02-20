# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，
# 所以在读取中文时会报错。

# 给定两个数组，编写一个函数来计算它们的交集。
#
# 示例 1:
#
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]
# 示例 2:
#
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [4,9]
# 说明：
#
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
# 我们可以不考虑输出结果的顺序。
# 进阶:
#
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？


# 如果输出两个[2]     # 答案
# def intersect(self, nums1, nums2):
#     """
#     :type nums1: List[int]
#     :type nums2: List[int]
#     :rtype: List[int]
#     """
#     inter = set(nums1) & set(nums2)
#     l = []
#     for i in inter:
#         l += [i] * min(nums1.count(i), nums2.count(i))        min在两个数组的最小值
#     return l


# 如果是输出一个[2] # 答案
# def intersection(self, nums1, nums2):
#     """
#     :type nums1: List[int]
#     :type nums2: List[int]
#     :rtype: List[int]
#     """
#     return list(set(nums1) & set(nums2))


# 以前/自己 现在      思路不太好 remove时容易出现角标越界
# def intersect(a, b):
#     c = []
#     if len(a) > len(b):
#         for i in range(0, len(b)):
#             for x in range(0, len(a)):
#                 if b[i] == a[x]:
#                     c.append(b[i])
#                     a.remove(a[x])
#                     # b.remove(b[i])
#                     break
#     return c

# if __name__ == "__main__":
#     a = [1,3, 4, 5, 2]
#     b = [2,4, 6,2]
#     print(intersect(a, b))