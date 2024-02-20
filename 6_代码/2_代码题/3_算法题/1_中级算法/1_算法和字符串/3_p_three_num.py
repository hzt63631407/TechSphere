# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 三数之和
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


# 自己 用这种方法
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    a = []
    if (not nums or n < 3):
        return []
    for i in range(len(nums)):
        if nums[i] > 0:
            return a
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            if nums[i] + nums[l] + nums[r] == 0:
                if [nums[i], nums[l], nums[r]] not in a:
                    a.append([nums[i], nums[l], nums[r]])
            if nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            else:
                l += 1
    return a


# 答案
# 排序 + 双指针
# [-2,-1,-1,0,1,2,3]
# 本题的难点在于如何去除重复解。
# https://leetcode-cn.com/problems/3sum/solution/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
# def threeSum(nums: list):
#     n = len(nums)
#     res = []
#     if (not nums or n < 3):
#         return []
#     nums.sort()
#     res = []
#     for i in range(n):
#         if (nums[i] > 0):
#             return res
#         if (i > 0 and nums[i] == nums[i - 1]):
#             continue
#         L = i + 1                                                 # 双指针+排序
#         R = n - 1
#         while (L < R):
#             if (nums[i] + nums[L] + nums[R] == 0):
#                 res.append([nums[i], nums[L], nums[R]])
#                 while (L < R and nums[L] == nums[L + 1]):         # 3个数相同 如a 可以去掉
#                     L = L + 1
#                 while (L < R and nums[R] == nums[R - 1]):
#                     R = R - 1
#                 L = L + 1
#                 R = R - 1
#             elif (nums[i] + nums[L] + nums[R] > 0):              # 用elif
#                 R = R - 1
#             else:
#                 L = L + 1
#     return res





# 每个人向主持人登记自己要找的配对，如果登记时，自己要找的配对已经登记过了，则成功
def two_num_2(a, target):
    # 时间复杂度 2n
    l1 = []
    l2 = []
    count = 0
    for i in a:
        if i in l1:
            l2.append([])
            l2[count].append(i)
            l2[count].append(target - i)
            count += 1
        else:
            l1.append(target - i)
    return l2



# 没有进行去重
def three_num_2(a, target):
    # 时间复杂度 n^2
    l1 = []
    l2 = []
    count = 0
    cou = 0
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if i < j:
                l1.append([])
                l1[count].append(target - a[i] - a[j])
                l1[count].append(i)
                l1[count].append(j)
                count += 1
        for k in range(0, count):
            if a[i] == l1[k][0]:
                if i != l1[k][1] and i != l1[k][2] and i < l1[k][2]:
                    l2.append([])
                    l2[cou].append(l1[k][0])
                    l2[cou].append(a[l1[k][1]])
                    l2[cou].append(a[l1[k][2]])
                    cou += 1
    return l2

    # return l1


if __name__ == "__main__":
    a = [-1, -1, 2,-1, 2, 3, 4, 1, 0, -2, 1]
    b = [-1, 0, 1, 2, -1, -4]
    # print(two_num_1(a, 2))
    # print(two_num_2(a, 2))
    # print(three_num_1(a, 0))
    print(threeSum(a))
