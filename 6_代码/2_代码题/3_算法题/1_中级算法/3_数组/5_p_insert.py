# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
#
#  
#
# 示例 1：
#
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]


# intervals+newInterval 组成新数组
# def merge(self, intervals: list) :
#     intervals.sort()
#     res = [intervals[0]]
#     for i in intervals[1:]:
#         if res[-1][1] >= i[0]:                             # 坐标0不用比,因为0一定是前面的小
#             res[-1][1] = max(i[1], res[-1][1])
#         else:
#             res.append(i)
#     return res

