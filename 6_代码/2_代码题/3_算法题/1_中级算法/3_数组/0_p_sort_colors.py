
# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# leetcode 75
# 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，
#
# 使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 必须在不使用库的sort函数的情况下解决这个问题。

# 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]

# 答案

# 遍历 如果是0，交换位置
# 从1的开始位置，再遍历，如果是1，交换位置

def sortColors(self, nums: list) -> None:
    n = len(nums)
    ptr = 0
    for i in range(n):
        if nums[i] == 0:                                    # 如果等于0，和ptr交换，ptr是最前的，每次+1
            nums[i], nums[ptr] = nums[ptr], nums[i]         # 同时执行,交换
            ptr += 1
    for i in range(ptr, n):
        if nums[i] == 1:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1

a = 1
b = 2
a,b = b,a
print(a,b)