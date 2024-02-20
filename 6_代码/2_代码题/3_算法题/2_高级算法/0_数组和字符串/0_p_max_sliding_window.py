# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值。
#
# 示例:
#
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# 提示：
#
# 你可以假设k总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
#
# 进阶：
#
# 你能在线性时间复杂度内解决此题吗？


# 超时    没有时间要求用这个
def maxInWindows(self, num: List[int], size: int) -> List[int]:
    # write code here
    temp = 0
    ans = []
    l = 0
    for i in range(len(num) - size + 1):
        a = num[i:i + size]
        temp = max(a)
        ans.append(temp)
    return ans


# 自己
# 外循环0，len-k的元素
# 内循环开始i，到k结束
# 找出这个数组的最大值
# 把数组的最大值存起来再输出

# 如果有时间要求用这个
def maxInWindows(self, num, size):
    # write code here
    #         双端队列
    queue = []
    #         返回列表
    res = []
    i = 0
    while size > 0 and i < len(num):
        if len(queue) > 0 and i - size + 1 > queue[0]:  # 超出范围的去掉
            queue.pop(0)
        #             当前值大于之前的值，之前的不可能是最大值，可以删掉
        while len(queue) > 0 and num[queue[-1]] < num[i]:
            queue.pop()
        #             进入队列
        queue.append(i)
        if i >= size - 1:  # 此时开始是第一个滑动窗口
            res.append(num[queue[0]])
        i += 1
    return res


# 自己的解法没有在线性时间复杂度内解决此题 超时
def max_sliding_window(nums,k):
    temp = []
    output = []
    for i in range(0, len(nums)-k+1):
        for j in range(i, i+k):
            temp.append(nums[j])
        t = max(temp)
        output.append(t)
        temp = []
    return output

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(max_sliding_window(nums,k))


# 超时
def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    res = list()                        # 等同于res = []
    if not nums:
        return res
    for i in range(len(nums) - k + 1):
        j = i + k
        res.append(max(nums[i:j]))      # 直接从原来的数组里max最大值，不需要新建一个数组进行循环
    return res


# 自己 三个数相加
# def max_sliding_window(nums, k):
#     l = []
#     s = 0
#     for i in range(0, len(nums) - k +1):
#         for j in range(0, k):
#             s = s + nums[i + j]
#         l.append(s)
#         s = 0
#     return l



# 自己最大值
# def max_sliding_window(nums, k):
#     l1 = []
#     l2 = []
#     s = 0
#     for i in range(0, len(nums) - k+1):
#         for j in range(0, k):
#             l1.append(nums[i+j])
#         l2.append(max(l1))
#     return l2

if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    print(max_sliding_window(nums, 3))
