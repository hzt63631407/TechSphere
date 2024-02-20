

# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。
# 请你从 nums 中选出三个整数，使它们的和与 target 最接近。
#
# 返回这三个数的和。
#
# 假定每组输入只存在恰好一个解。

# 自己
def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    t = 0
    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            three_sum = nums[i] + nums[l] + nums[r]
            if three_sum == target:
                return target
            if t == 0 or abs(three_sum - target) < t:      # 第一次没有值，所以先附值
                t = abs(three_sum - target)
                three_min = three_sum
            if nums[i] + nums[l] + nums[r] > target:
                r -= 1
            elif nums[i] + nums[l] + nums[r] < target:
                l += 1
    return three_min




def threeSumClosest(self, nums: List[int], target: int) -> int:
    n = len(nums)
    nums.sort()
    re_min = 0  # 存储当前最小的差值
    for i in range(n):
        low = i + 1
        high = n - 1
        while low < high:
            three_sum = nums[i] + nums[low] + nums[high]
            x = target - three_sum  # 当前三数的差值
            if re_min == 0:
                re_min = abs(x)      # 继续用re_min 存储
                sum_min = three_sum  # sum_min为当前最接近的和

            if abs(x) < re_min:
                re_min = abs(x)
                sum_min = three_sum

            if three_sum == target:
                return target
            elif three_sum < target:
                low += 1
            else:
                high -= 1

    return sum_min