# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 问总共有多少条不同的路径？
#
#
#
# 例如，上图是一个7 x 3 的网格。有多少可能的路径？
#
# 说明：m 和 n 的值均不超过 100。
#
# 示例 1:
#
# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
# 示例 2:
#
# 输入: m = 7, n = 3
# 输出: 28


# 自己
# 递归 在最下边或者最右边只有一种走法，其余没一格都是两种走法。
def unique_paths(m, n):
    if m == 1 or n == 1:
        return 1
    return unique_paths(m-1,n) + unique_paths(m, n-1)



# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。
#
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
#
# 网格中的障碍物和空位置分别用 1 和 0 来表示

def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    if obstacleGrid[0][0] == 1:
        return 0
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        if obstacleGrid[i][0] == 1:
            break
        dp[i][0] = 1

    for i in range(n):
        if obstacleGrid[0][i] == 1:
            break
        dp[0][i] = 1

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] != 1:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]













# 自己 以前
# def uniquePaths(m, n):
#     """
#     :type m: int
#     :type n: int
#     :rtype: int
#     # """
#     # m1 = m - 1
#     # n1 = n - 1
#     # if m1 == 1 or n1 == 1:
#     if m == 1 or n == 1:
#         return 1
#     else:
#         return uniquePaths(m - 1, n) + uniquePaths(m, n - 1)


if __name__ == "__main__":
    print(unique_paths(7, 3))
