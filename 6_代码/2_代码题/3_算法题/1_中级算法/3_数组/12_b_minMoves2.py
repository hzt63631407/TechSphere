

# 462. 最少移动次数使数组元素相等 II
#
# 给你一个长度为 n 的整数数组 nums ，返回使所有数组元素相等需要的最少移动数。
#
# 在一步操作中，你可以使数组中的一个元素加 1 或者减 1 。
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：2
# 解释：
# 只需要两步操作（每步操作指南使一个元素加 1 或减 1）：
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]



# 将数组从小到大排序，假设tar是每个数最后都要移动到的平均数，那么在tar左边的数，
#
# 每个数移动的步数是tar - num[left]（0 < left < mid）,
#
# 在tar右边的数，移动的步数是 num[right] - tar ( len(nums - 1)> right >= mid)
#
# 那么移动的总次数res = tar - num[0] + tar - num[1] + ... num[right] - tar 最后发现就是双指针左右相减的和加起来。

# 那么无论 target 选择何值，对于数组的最小值和最大值而言，
# 它们移动到 target 的次数之和一定是固定的！都等于 最大值 - 最小值。


# [1,10,100] 1和100的和是固定的，10是中间值，所以取10

def minMoves2(self, nums: List[int]) -> int:
    nums.sort()
    res = 0
    for i in range(len(nums)):
        if nums[i] < nums[len(nums) // 2]:
            res += nums[len(nums) // 2] - nums[i]
        elif nums[i] > nums[len(nums) // 2]:
            res += nums[i] - nums[len(nums) // 2]
    return res



# def minMoves2(self, nums: List[int]) -> int:
#     nums.sort()
#     m = nums[len(nums) // 2]
#     l = 0
#     r = len(nums) - 1
#     s = 0
#     while l < r:
#         s += nums[r] - m
#         s += m - nums[l]
#         l += 1
#         r -= 1
#     return s

