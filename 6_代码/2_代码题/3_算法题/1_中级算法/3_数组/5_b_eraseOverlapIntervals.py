
# leetcode 435

# 给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。
#
# 返回 需要移除区间的最小数量，使剩余区间互不重叠 。
#
# 示例 1:
#
# 输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
# 输出: 1
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。


# 1）由于区间集合经过排序，所以判断一个区间是否移除只需要参考它左边的区间；
# 2）对于有重叠的区间，优先选择右区间end更小的区间，移除end较大的区间（贪心思想，减小与后面区间重叠的可能)
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort()
    ans = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            ans += 1
            if intervals[i][1] > intervals[i-1][1]:             # 如果后面的大，要移除后面的
                intervals[i] = intervals[i-1]                   # 如果前面的大，保持，继续判断，因为可以+1
    return ans



def eraseOverlapIntervals(self, intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])
    l = len(intervals)
    count = 1
    end = intervals[0][1]
    for i in range(1, l):
        if intervals[i][0] >= end:                      # 如果后面的开头比前面一个末尾大，说明不能删 +1
            count += 1
            end = intervals[i][1]
    return l - count


