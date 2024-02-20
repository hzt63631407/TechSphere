
# 485. 最大连续 1 的个数
# 给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。
#
# 示例 1：
#
# 输入：nums = [1 ,1 ,0 ,1 ,1 ,1]
# 输出：3
# 解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.


def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    l = 0
    m = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            l += 1
        else:
            l = 0
        if l > m :
            m = l
    return m