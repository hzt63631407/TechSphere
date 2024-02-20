# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。



# 超时
def largestRectangleArea(heights) :
    l = []
    a = []
    for i in range(0, len(heights)):
        for j in range(i + 1, len(heights)+1):
            l.append(heights[i:j])
    print(l)
    for i in l:
        s = min(i) * len(i)                 # 数组里最小的*数组的长度
        # s = min(i[0],i[-1]) * (len(i)-1)      # 数组里最小的*数组的长度
        a.append(s)
    return a


def largestRectangleArea(self, heights: List[int]) -> int:
    size = len(heights)
    res = 0
    heights = [0] + heights + [0]
    # 先放入哨兵结点，在循环中就不用做非空判断
    stack = [0]
    size += 2
    for i in range(1, size):
        while heights[i] < heights[stack[-1]]:
            cur_height = heights[stack.pop()]
            cur_width = i - stack[-1] - 1
            res = max(res, cur_height * cur_width)
        stack.append(i)
    return res




print(largestRectangleArea([2,1,5,6,2,3]))
# print(largestRectangleArea([1,8,6,2,5,4,8,3,7]))

