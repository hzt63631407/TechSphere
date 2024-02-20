# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。
#
# leetcode 347
# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
#
#  
#
# 示例 1:
#
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 示例 2:
#
# 输入: nums = [1], k = 1
# 输出: [1]

# 答案
def topKFrequent(nums,k):
    d = {}
    ans = []
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = 1
        else:
            d[nums[i]] += 1
    a = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for i in range(k):
        ans.append(a[i][0])
    return ans

print(topKFrequent([2,2,3,2,3,2,2,1,2,4,4],3))


# https://www.runoob.com/python/python-func-sorted.html     sorted函数



