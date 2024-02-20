# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# leetcode 11
# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
#
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 返回容器可以储存的最大水量。
#
# 说明：你不能倾斜容器。

# https://leetcode-cn.com/problems/container-with-most-water/

# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
# 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

# 输入：height = [1,1]
# 输出：1


# 答案    # 双指针
def maxArea(self, nums: List[int]) -> int:
    l = 0
    r = len(nums) - 1
    res = 0
    while l < r:
        a = (r - l) * min(nums[l], nums[r])
        if res < a:
            res = a
        if nums[l] > nums[r]:
            r -= 1
        else:
            l += 1
    return res


# 自己思路
# def maxArea(self, height: list) -> int:
#     l = []
#     a = []
#     for i in range(0, len(heights)):
#         for j in range(i + 1, len(heights)+1):
#             l.append(heights[i:j])
#     print(l)
#     for i in l:
#         s = min(i[0],i[-1]) * (len(i)-1)
#         a.append(s)
#     return a
