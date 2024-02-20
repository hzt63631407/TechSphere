

# leetcode 213
# 一个专业的小偷，计划偷窃一个环形街道上沿街的房屋，每间房内都藏有一定的现金。
# 这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
# 同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警


def rob(self, nums: List[int]) -> int:
    if len(nums ) == 1:
        return nums[0]
    def dp_nums(nums)  :##正常的房屋偷盗
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]
    return max(dp_nums(nums[1:]) ,dp_nums(nums[:-1]))




# 相比较之前的房屋偷盗就多了一个限制条件，最后一个不能和第一个连接。
# 分类讨论 1.去掉第一个 2.去掉最后一个 最后max一下

