# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# leetcode 剑值010
# 给你一个整数数组 nums 和一个整数 k ，
# 请你统计并返回 该数组中和为 k 的子数组的个数 。
# (子数组，连续的字符串)（子集，子序列，不用连续）
#
# 示例 1：
#
# 输入：nums = [1,1,1], k = 2
# 输出：2
# 示例 2：
#
# 输入：nums = [1,2,3], k = 3
# 输出：2

# https://blog.csdn.net/weixin_41729258/article/details/106142249
# 解题方法：
# 1、暴力求解，两次遍历数组得到最终结果，时间复杂度为0(n^2)，在C语言及C++中可以通过，但是在python中是超出时间限制了的。
#
# 2、通过hash表储存从前到后的和，从而利用增加空间复杂度，
# 减小时间复杂度，时间复杂度为0(n)，空间复杂度也为0(n)。

# 前缀和  前缀值-target 得到的值，就是去（前缀和）减去（得到的值）的数组 的剩下的数组
# 比如 1,2,3,4,5 前缀和2是15，target的是9，那么前缀和去除掉最开始的前缀和1也就是6，剩下的数组4，5就是答案
#解法二：正解，通过Hash表（字典），求得
# class Solution(object):
#     def subarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         res = {0:1}                           # 如果sum-k==0，那么就有1个
#         sums = 0
#         ans = 0
#         for i in nums:
#             sums += i
#             if (sums-k) in res:               # 如果目标的sum-k 在res里面       那么结果加上sum-k的数值
#                 ans += res[sums-k]
#             if sums in res:
#                 res[sums] += 1                # 如果sums在里面 原来数值+1
#             else:
#                 res[sums] = 1                 # 如果原来数值不在，附值为1
#         return ans

#暴力求解，超出时间复杂度
# 答案
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        ans = 0
        for i in range(n):
            res = 0
            for j in range(i,n):
                res += nums[j]
                if res == k:
                    ans += 1
        return ans

