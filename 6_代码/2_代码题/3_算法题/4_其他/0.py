# -*- coding: utf-8 -*-

# 有三种颜色的小球: 红, 绿, 蓝. 任意两个小球可以融合成一个新的小球. 颜色的融合规则如下:
# 1. 两个相同颜色融合后保持原来的颜色, 例: 红色 + 红色 = 红色
# 2. 两个不同颜色融合后会生成第三个颜色, 例: 红色 + 绿色 = 蓝色
# 请设计一个程序来解决任意个数小球合并后, 得到的小球颜色, 例:

# 红球 + 红球 + 绿球 + 蓝球  -> 蓝球
# 红球 + 绿球 + 红球 + 蓝球  -> 红球


def te(nums):
    for i in range(1, len(nums)):
        # print(i)
        if nums[i-1] == nums[i]:
            nums[i] = nums[i-1]
            # print(nums[i])
        elif (nums[i] == 0 and nums[i - 1] == 1) or (nums[i] == 1 and nums[i - 1] == 0):
             nums[i] = 2
        elif (nums[i] == 1 and nums[i - 1] == 2) or (nums[i] == 2 and nums[i - 1] == 1):
             nums[i] = 0
        elif (nums[i] == 0 and nums[i - 1] == 2) or (nums[i] == 2 and nums[i - 1] == 0):
             nums[i] = 1
    return nums[-1]

ans = print(te([0,2,2,1]))

