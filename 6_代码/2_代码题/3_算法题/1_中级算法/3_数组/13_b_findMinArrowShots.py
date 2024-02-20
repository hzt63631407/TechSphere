
# 452. 用最少数量的箭引爆气球
#
#
# 输入：points = [[10,16],[2,8],[1,6],[7,12]]
# 输出：2
# 解释：气球可以用2支箭来爆破:
# -在x = 6处射出箭，击破气球[2,8]和[1,6]。
# -在x = 11处发射箭，击破气球[10,16]和[7,12]。

# 贪心，
# 每次射箭尽量找气球有重叠的点。排序后，记录重叠区间，
# 下一个气球有重叠就进一步取交集，不重叠就结果+1


# 自己
# 如果是[1,6][3,8] 那么合并之后应该是[3,6],因为需要在3,6之间射箭，最后返回需要有多少个区间进行射箭即可
def findMinArrowShots(self, points: List[List[int]]) -> int:
    points.sort()
    a = [points[0]]
    for i in range(1, len(points)):
        if a[-1][1] >= points[i][0]:
            a[-1][0] = points[i][0]
            a[-1][1] = min(a[-1][1], points[i][1])
        else:
            a.append(points[i])
    return len(a)



# [1,6][2,8]的交集 [2,6]  没有交集就更新初始结果

def findMinArrowShots(self, points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    if len(points) == 0:
        return 0
    points = sorted(points, key=lambda x: x[0])
    start = points[0][0]
    end = points[0][1]
    res = 0
    for point in points:
        if point[0] <= end:
            start = max(point[0], start)
            end = min(point[1], end)
        else:
            res += 1
            start = point[0]
            end = point[1]
    return res + 1
