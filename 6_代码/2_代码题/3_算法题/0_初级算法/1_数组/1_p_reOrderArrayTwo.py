# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 描述
#
# 输入一个长度为 n 整数数组，数组里面可能含有相同的元素，
# 实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前面部分，
# 所有的偶数位于数组的后面部分，对奇数和奇数，偶数和偶数之间的相对位置不做要求，
# 但是时间复杂度和空间复杂度必须如下要求。


class Solution:
    def reOrderArrayTwo(self , array: List[int]) -> List[int]:
        # write code here
        array.sort(key=self.rule)
        return array
    def rule(self,m):
        if  m % 2 == 0:
            return 1
        else:
            return 0