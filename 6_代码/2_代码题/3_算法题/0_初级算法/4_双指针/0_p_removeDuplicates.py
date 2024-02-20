

# leetcode 26. 删除有序数组中的重复项

# 给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，
# 使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。

# 答案
# 因为给定数组是有序的，所以相同元素必然连续。我们可以使用双指针解决本题，
# 遍历数组检查每一个元素是否应该被保留，如果应该被保留，就将其移动到指定位置。


# num[j]是新数组，num[i]需要判断是否要加入，
# 如果和nums[j-1]不相等，则新的值num[j]=num[i] j+1

# 需要把新的值赋值给空数组
def removeDuplicates(self, nums: List[int]) -> int:
    j = 1
    for i in range(1, len(nums)):
        if nums[j-1] != nums[i]:
            nums[j] = nums[i]
            j += 1
    return j



