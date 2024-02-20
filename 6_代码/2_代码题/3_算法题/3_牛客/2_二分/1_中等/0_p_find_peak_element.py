# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 峰值元素是指其值大于左右相邻值的元素。
#
# 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
#
# 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
#
# 你可以假设 nums[-1] = nums[n] = -∞。
#
# 示例 1:
#
# 输入: nums = [1,2,3,1]
# 输出: 2
# 解释: 3 是峰值元素，你的函数应该返回其索引 2。
# 示例 2:
#
# 输入: nums = [1,2,1,3,5,6,4]
# 输出: 1 或 5
# 解释: 你的函数可以返回索引 1，其峰值元素为 2；
#      或者返回索引 5， 其峰值元素为 6。
# 说明:
#
# 你的解法应该是 O(logN) 时间复杂度的。


# 由于题目假设nums[-1]=nums[n]=-∞。所以，我们从0开始往后遍历元素，如果某个元素大于其后面的元素，则该元素就是峰值元素。（但是它时O(n)，不符合题意）
#
# O(logN)一般考虑二分搜索。有如下规律：i=mid
#
# 规律一：如果nums[i] > nums[i+1]，则在i之前一定存在峰值元素
#
# 规律二：如果nums[i] < nums[i+1]，则在i+1之后一定存在峰值元素


# 答案
def findPeakElement(self, nums):
    l = 0
    r = len(nums) - 1
    while (l < r):
        mid = (l+r) // 1
        if nums[mid] > nums[mid + 1]:  # 当mid大于mid+1的时候,在[0,mid]一定存在一个峰值
            r = mid
        else:
            l = mid + 1
    return l                            # 返回最后一个元素

# 当nums[mid]大于nums[mid+1]的时候,在[0,mid]一定存在一个峰值？？？？

# 因为如果nums[mid]不是峰值的话,nums[mid-1]就要大于nums[mid]，
# 同理如果nums[mid-1]不是峰值的话,nums[mid--2]就要大于nums[mid-1]，
# 就是保证不能出现拐点，但是这样下去，0一定时拐点，因为nums[-1] = -∞,所以在[0,mid]一定存在一个峰值。


# 自己 不是logN解法
def find_peak_element(list):
    if len(list) == 0 & len(list) == 1:
        return -1
    for i in range(0, len(list)-2):
        if list[i] < list[i+1]:
            if list[i+1] > list[i+2]:
                return list[i+1]
    return -1


list1 = [1]
list2 = [1,2]
list3 = [1,2,3,1]
print(find_peak_element(list1))
print(find_peak_element(list2))
print(find_peak_element(list3))