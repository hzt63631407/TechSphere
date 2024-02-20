# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

# 自己
# 两次循环就可以解决，想想一次循环可以解决嘛？

# 可以！ 找出一个 然后用in！

# 答案
def FindNumbersWithSum(self , array: List[int], sum: int) -> List[int]:
     res = []
     dict = {}
     for i in range(len(array)):
         t = sum - array[i]
         if t not in dict:
             dict[array[i]] = i
         else:
             res.append(array[i])
             res.append(t)
             break
     return res


a = [3, 2, 11, 15, 7]
b = 9
print(twoSum(a, b))



# 给定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。
def twoSum(self, nums: List[int], target: int) -> List[int]:
    l = 0
    r = len(nums) - 1
    while l < r:
        if nums[l] + nums[r] > target:
            r = r - 1
        if nums[l] + nums[r] < target:
            l = l + 1
        if nums[l] + nums[r] == target:
            return l, r



