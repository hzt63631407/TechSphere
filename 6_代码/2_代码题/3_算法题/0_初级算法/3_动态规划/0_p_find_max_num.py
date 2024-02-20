# -*- coding: utf-8 -*-

# leetcode 53
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

# 使用动态规划特征：
# 1. 求一个问题的最优解
# 2. 大问题可以分解为子问题，子问题还有重叠的更小的子问题             # 动态规划的思想是递归
# 3. 整体问题最优解取决于子问题的最优解（状态转移方程）
# 4. 从上往下分析问题，从下往上解决问题
# 5. 讨论底层的边界问题

# 数组排序
# a = [1,2,-1,3,-2,-1]
# a.sort()
# print(a)

# https://leetcode-cn.com/problems/maximum-subarray/solution/dong-tai-gui-hua-fen-zhi-fa-python-dai-ma-java-dai/
# 答案思路
# 1.假设答案的坐标是i，那么i一定从0到8产生。      # len(a)是9 所以i是0到8
# 2.所以求以i结尾的8个数最大值，然后把这8个子问题的得出最大的值进行比较，最大的就是最大值。
# 3.m[0] = -2
# 4.m[1] = -2+1 或者 m[1] = 1
# 5.如果编号为 i 的子问题的结果是负数或者0，
# 那么编号为 i + 1 的子问题就可以把编号为 i 的子问题的结果舍弃掉（这里 i 为整数，最小值为 1 ，最大值为 8）
# 6.比如：m[3]的最优解先是判断一下m[2]是否大于0，如果大于0，那么就加上a[3],如果小于0，那么就是a[3]，得出的结果再和m[2]对比一下，大的就是m[3].
# 7.注意：需要把每次获得的值m[i]存储，有新的m[i]产生时，进行判断。


# 最优子结构 m[8] = m[7] or a[7] ,m[7] = m[6] or a[7]
# 边界 m[0] = -2,m[1] = m[0] or a[1] = a[1]

# 答案是一个数组或者每次将结果进行比较，只记录最大


# 按照这个思路
# 答案 题解
def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
     """
    for i in range(1, len(nums)):
        nums[i] = nums[i] + max(nums[i - 1], 0)
    return max(nums)

a = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(a))

# class Solution:
#     def FindGreatestSumOfSubArray(self, array: List[int]) -> List[int]:
#         # write code here
#         maxval = array[0]
#         temp = array[0]  # 序列累加
#         endindex = 1
#         beginindex = 0
#         for i in range(1, len(array)):
#             if temp < 0:
#                 temp = array[i]
#                 beginindex = i
#             else:
#                 temp += array[i]
#             if temp >= maxval:
#                 endindex = i
#                 maxval = temp
#         # begin > end 表示 序列全为负
#         # begin不断累加， 但此时end已保存最大值索引
#         if beginindex > endindex:
#             return array[endindex:endindex + 1]
#         return array[beginindex:endindex + 1]

# 自己 以前
def findMaxSum(num):
    temp = 0
    res = num[0]
    for i in range(0, len(num)):
        temp += num[i]
        if temp > res:
            res = temp
        elif temp < 0:
            temp = 0
    return res



a = [-2,1,-3,4,-1,2,1,-5,4]
print(findMaxSum(a))