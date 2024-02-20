
# 统计一个数字在排序数组中出现的次数。

# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: 0
# 剑值offer 53

# 二分都是分治思想


# 答案
def search(self, nums: List[int], target: int) -> int:
    def left_func(nums, target):
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = (left + right) // 2
            if nums[mid] >= target:                         # 注意这里  画图，因为求左边坐标，所以mid>=target
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1
        return left

    a = left_func(nums, target)
    b = left_func(nums, target + 1)
    # # if a == len(nums) or nums[a] != target:                 # a的角标在最右边，或者nums[a]不存在
    # #     return 0
    # else:
    return b - a