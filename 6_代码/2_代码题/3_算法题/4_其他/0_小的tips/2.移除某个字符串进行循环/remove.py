# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。



def remove(nums):
    for i in range(0, len(nums)):
        l = nums[:i] + nums[i+1:]             # 每次remove掉num[i]
        print(l)


remove([1,2,3])