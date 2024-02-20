
# 描述
# 给出一组区间，请合并所有重叠的区间。
# 请保证合并后的区间按区间起点升序排列。
#
# 示例1
# 输入：
# [[10,30],[20,60],[80,100],[150,180]]
# 返回值：
# [[10,60],[80,100],[150,180]]


class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        intervals.sort(key=lambda x: x.start)
        a = [intervals[0]]
        for i in intervals[1:]:
            if a[-1].end >= i.start:
                a[-1].end = max(a[-1].end, i.end)
            else:
                a.append(i)
        return a