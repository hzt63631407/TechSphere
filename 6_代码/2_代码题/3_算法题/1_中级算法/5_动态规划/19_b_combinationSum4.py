

# 给定一个由 不同 正整数组成的数组 nums ，和一个目标整数 target 。
# 请从 nums 中找出并返回总和为 target 的元素组合的个数。
# 数组中的数字可以在一次排列中出现任意次，但是顺序不同的序列被视作不同的组合。


# 输入：nums = [1,2,3], target = 4
# 输出：7
# 解释：
# 所有可能的组合为：
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)



# 因此在计算dp[i]时,应该计算所有dp[i-num]的和。
# 答案
def combinationSum4(self, nums: List[int], target: int) -> int:
    dp = [1] + [0] * target
    for i in range(1, target + 1):
        for num in nums:
            if num <= i:
                dp[i] += dp[i - num]

    return dp[target]
