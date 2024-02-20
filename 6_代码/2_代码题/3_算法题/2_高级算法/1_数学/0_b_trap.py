
# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。


# 42. 接雨水
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。


# https://leetcode-cn.com/problems/trapping-rain-water/comments/

# 我来解释一下这个优秀的思路吧
# h1, h2一个从左往右遍历，一个从右往左遍历，二者都会经过最大值，交汇这里也就形成了一个len(height) * 最大高度值的矩形，
# 而剩下部分就是刚好包络原图形的部分，这里包络线在形成过程中，不能向下走，所以包络部分减去黑色原图就是答案

# 你是怎么想到从左边遍历加从右边遍历等于总面积加原来图像加雨水数的...
# def trap(self, height: List[int]) -> int:
#     ans = 0
#     h1 = 0
#     h2 = 0
#     for i in range(len(height)):
#         h1 = max(h1, height[i])
#         h2 = max(h2, height[-i - 1])
#         ans = ans + h1 + h2 - height[i]
#     return ans - len(height) * h1