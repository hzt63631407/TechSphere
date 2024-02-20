# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
#
# 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

#  leetcode 56
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
#
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。


# 答案
def merge(intervals: list) :
    intervals.sort()
    res = [intervals[0]]
    for i in intervals[1:]:
        if res[-1][1] >= i[0]:                             # 坐标0不用比,因为0一定是前面的小
            res[-1][1] = max(i[1], res[-1][1])
        else:
            res.append(i)
    return res


list = [[1,4],[2,3],[1,2],[2,4],[3,6],[3,5]]                # start的最小值排序 [1,4]在[2,3]前面
list.sort()
print(list)
print(merge(list))


# class Interval:
#     def __init__(self, a=0, b=0):
#         self.start = a
#         self.end = b

def merge(self, intervals: List[Interval]) -> List[Interval]:
    # write code here
    intervals.sort(key=lambda x: x.start)
    a = [intervals[0]]
    for i in intervals[1:]:
        if a[-1].end >= i.start:
            a[-1].end = max(a[-1].end, i.end)
        else:
            a.append(i)
    return a