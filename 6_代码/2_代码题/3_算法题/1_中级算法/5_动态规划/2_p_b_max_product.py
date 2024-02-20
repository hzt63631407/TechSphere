# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 乘积最大子序列
# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
#
# 示例 1:
#
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 示例 2:
#
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

# 答案
# 1.数列中没有0.容易证明如果数列中没有0，最大乘积区间必定是触及边界的（或包含左边界，或包含右边界），
# 这样正反两个累积数列必然包括最大值。
# 2.数列中有0.包括两个情况：
# a。最大乘积区间就是0本身；
# b。最大乘积区间是视一个个0为一个个边界（因为如果跨了0，则乘积为0，包含在情况a中），
# 在每个内部区间会满足1中条件——必然触及边界，或左边界或右边界，
# 这样正反两个累积数列又恰好解决。只能说是神仙代码

# 答案  # 数学方法
def maxProduct(self, A: List[int]) -> int:
    B = A[::-1]
    for i in range(1, len(A)):
        A[i] *= A[i - 1] or 1
        B[i] *= B[i - 1] or 1
    return max(max(A), max(B))


def max_product(a):
    l1 = []
    max = a[0]
    for i in range(0, len(a)):                  # 找出所有的连续字符串
        for j in range(0, len(a) + 1):
            if i < j:
                l = a[i:j]
                l1.append(l)
    for i in l1:                                # 计算乘积
        t = 1
        for k in i:
            t = t * k
        if t > max:
            max = t
    return max




# 自己
# def maxProduct(nums):
#     l = []
#     sum = 1
#     for i in range(0, len(nums)):
#         for j in range(0, len(nums)):
#             if i <= j:
#                 s = nums[i:j+1]
#                 for k in s:
#                     sum = sum * int(k)
#                 l.append(sum)
#                 sum = 1
#
#     return l


if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    # nums = [-2, 0, -1]
    # print(nums[0:2])
    print(max_product(nums))
