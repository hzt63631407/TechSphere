# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。


# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
# 示例 1：
#
#
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。

# https://leetcode-cn.com/problems/maximal-rectangle/comments/

# 答案
# class Solution:
#     def maximalRectangle(self, matrix: List[List[str]]) -> int:
#         if not matrix or not matrix[0]:
#             return 0
#         nums = [int(''.join(row), base=2) for row in matrix] #先将每一行变成2进制的数字
#         ans, N = 0, len(nums)
#         for i in range(N):#遍历每一行，求以这一行为第一行的最大矩形
#             j, num = i, nums[i]
#             while j < N: #依次与下面的行进行与运算。
#                 num = num & nums[j]  #num中为1的部分，说明上下两行该位置都是1，相当于求矩形的高，高度为j-i+1
#                 # print('num=',bin(num))
#                 if not num: #没有1说明没有涉及第i到第j行的竖直矩形
#                     break
#                 width, curnum = 0, num
#                 while curnum:
#                     #将cursum与自己右移一位进行&操作。如果有两个1在一起，那么cursum才为1，相当于求矩形宽度
#                     width += 1
#                     curnum = curnum & (curnum >> 1)
#                     # print('curnum',bin(curnum))
#                 ans = max(ans, width * (j-i+1))
#                 # print('i','j','width',i,j,width)
#                 # print('ans=',ans)
#                 j += 1
#         return ans