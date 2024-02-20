


# 描述
# 给定一个长度为 n 的非降序数组和一个非负数整数 k ，要求统计 k 在数组中出现的次数

def GetNumberOfK(self, nums: List[int], target: int) -> int:
    # write code here
    def left_func(nums, target):
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = (left + right) // 2
            if nums[mid] >= target:  # 注意这里  画图，因为求左边坐标，所以mid>=target
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