# # -*- coding: utf-8 -*-
# # Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。


# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#  
#
# 示例 1：
#
# 输入：[3,2,3]
# 输出：3
# 示例 2：
#
# 输入：[2,2,1,1,1,2,2]
# 输出：2


def majorityElement(nums: list):
    nums.sort()
    return nums[len(nums)//2]           # 因为一定有，排序后一定经过n/2


nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))




