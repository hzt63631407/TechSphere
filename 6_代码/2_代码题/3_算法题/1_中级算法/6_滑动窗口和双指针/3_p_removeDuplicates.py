


# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，
# 使每个元素 最多出现两次 ，返回删除后数组的新长度。
#
#
# 答案
# 因为给定数组是有序的，所以相同元素必然连续。我们可以使用双指针解决本题，
# 遍历数组检查每一个元素是否应该被保留，如果应该被保留，就将其移动到指定位置。

def removeDuplicates(self, nums: List[int]) -> int:
    j = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[j - 2]:
            nums[j] = nums[i]
            j += 1
    return j



