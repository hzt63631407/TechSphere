# # -*- coding: utf-8 -*-
# # Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。


# 有一个长度为 n 的非降序数组，比如[1,2,3,4,5]，将它进行旋转，即把一个数组最开始的若干个元素
# 搬到数组的末尾，变成一个旋转数组，比如变成了[3,4,5,1,2]，或者[4,5,1,2,3]这样的。
# 请问，给定这样一个旋转数组，求数组中的最小值。
#
# 要求:时间复杂度long n
# 剑值offer11
# 旋转不需要

# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        # 特殊情况判断
        if len(rotateArray) == 0:
            return 0
        # 左右指针
        i, j = 0, len(rotateArray) - 1
        while i < j:
            # 确定中点索引
            m = (i + j) // 2
            # m在左排序数组中，旋转点在 [m+1, j] 中
            if rotateArray[m] > rotateArray[j]: i = m + 1   # 需要+1
            # m在右排序数组中，旋转点在 [i, m] 中
            elif rotateArray[m] < rotateArray[j]: j = m             # 要用elif    # 注意这里
            else: j -= 1
        # 返回结果
        return rotateArray[i]

