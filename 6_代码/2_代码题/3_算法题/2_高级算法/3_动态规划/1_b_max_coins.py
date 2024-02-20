# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
#
# 现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。
#
# 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
#
# 求所能获得硬币的最大数量。
#
# 说明:
#
# 你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
# 0 ≤ n ≤ 500, 1 ≤ nums[i] ≤ 100
# 示例:
#
# 输入: [3,1,5,8]
# 输出: 167
# 解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#      coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167


# 答案
def maxCoins(self, nums: List[int]) -> int:
    n = len(nums)
    val = [1] + nums + [1]

    @lru_cache(None)
    def solve(left: int, right: int) -> int:
        if left >= right - 1:
            return 0

        best = 0
        for i in range(left + 1, right):
            total = val[left] * val[i] * val[right]
            total += solve(left, i) + solve(i, right)
            best = max(best, total)

        return best

    return solve(0, n + 1)


def max_coins(nums:list):

    #nums首尾添加1，方便处理边界情况
    nums.insert(0,1)
    nums.insert(len(nums),1)
    store = [[0]*(len(nums)) for i in range(len(nums))]
    print(store)

    def range_best(i,j):
        m = 0
        #k是(i,j)区间内最后一个被戳的气球
        for k in range(i+1,j): #k取值在(i,j)开区间中
            #以下都是开区间(i,k), (k,j)
            left = store[i][k]
            right = store[k][j]
            a = left + nums[i]*nums[k]*nums[j] + right
            if a > m:
                m = a
        store[i][j] = m

    #对每一个区间长度进行循环
    for n in range(2,len(nums)): #区间长度 #长度从3开始，n从2开始
        #开区间长度会从3一直到len(nums)
        #因为这里取的是range，所以最后一个数字是len(nums)-1

        #对于每一个区间长度，循环区间开头的i
        for i in range(0,len(nums)-n): #i+n = len(nums)-1

            #计算这个区间的最多金币
            range_best(i,i+n)
    print(store)
    return store[0][len(nums) - 1]


# 自己思路 用了回溯 答案是用动态规划
# def max_coins(nums):
#     result = []
#     def backtrack(nums,conis,track):
#         if nums == []:
#             result.append(conis)
#         for i in range(0, len(nums)):
#             if i == 0 :
#                 left = 1
#             else:
#                 left = nums[i-1]
#             if i == len(nums)-1:
#                 right = 1
#             else:
#                 right = nums[i+1]
#             t = nums[i]*left*right
#             conis = conis + t
#             print(conis)
#             print(nums[:i] + nums[i + 1:], conis, track + [nums[i]])
#     backtrack(nums,0,[])
#     return result








if __name__ == "__main__":
    nums = [3,1,5]
    print(max_coins(nums))
    # print(permute(num))
