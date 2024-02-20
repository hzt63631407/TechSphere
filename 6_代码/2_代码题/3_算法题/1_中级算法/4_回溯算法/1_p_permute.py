# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# leetcode 46
# 给定一个没有重复数字的序列，返回其所有可能的全排列。
# #
# # 示例:
# #
# # 输入: [1,2,3]
# # 输出:
# # [
# #   [1,2,3],
# #   [1,3,2],
# #   [2,1,3],
# #   [2,3,1],
# #   [3,1,2],
# #   [3,2,1]
# # ]


# 答案
# 思路介绍：使用递归对每一个位置进行遍历，以当前示例为例：刚开始我们的nums_all为[1,2,3]，而temp为[]，
# 我们第一次使用back函数时进入for循环会分别执行back([2,3],[1])，back([1,3],[2])和back([1,2],[3])，
# 之后分为三个分支再继续进行back函数的递归调用，直到back函数的第一个位置为空，则将得到的该结果添加到res中以便最后输出


# 有没有重复元素一样
def permute(nums):
    a = []
    l = len(nums)
    def backtrack(nums, track):
        if len(track) == l:
            if track not in a:
                    a.append(track)
        for i in range(0, len(nums)):
            backtrack(nums[:i]+nums[i+1:], track+[nums[i]])

    backtrack(nums,[])
    return a


# Python3 itertools 文档
#
# 一行代码:
#
# def permute(self, nums: List[int]) -> List[List[int]]:
#         return list(itertools.permutations(nums))


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    print(permute(a))
    # print(a[:0])
    # print(a[:1], a[2:], a[1])   # a[:1] 返回的是一个list a[1]返回的是一个值
