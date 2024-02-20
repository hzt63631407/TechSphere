# leetcode 283
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。


def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l = 0
    for i in range(len(nums)):
        # 当前元素!=0，就把其交换到左边，等于0的交换到右边
        if nums[i] != 0:
            nums[i], nums[l] = nums[l], nums[i]
            l += 1