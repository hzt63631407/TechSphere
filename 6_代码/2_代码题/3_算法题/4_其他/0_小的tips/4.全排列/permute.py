# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。



def permute(nums):
    a = []
    l = len(nums)
    def backtrack(nums, track):
        if len(track) == l:
            a.append(track)
        for i in range(0, len(nums)):
            backtrack(nums[:i]+nums[i+1:], track+[nums[i]])

    backtrack(nums,[])
    return a

print(permute([1,2,3]))
