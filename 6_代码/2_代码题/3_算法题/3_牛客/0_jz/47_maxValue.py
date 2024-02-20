
# 描述
# 在一个m\times nm×n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
# 你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、
# 直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
# 如输入这样的一个二维数组，
# [
# [1,3,1],
# [1,5,1],
# [4,2,1]
# ]
# 那么路径 1→3→5→2→1 可以拿到最多价值的礼物，价值为12

class Solution:
    def maxValue(self , grid: List[List[int]]) -> int:
        # write code here
            m = len(grid)
            n = len(grid[0])
            # 第一列只能来自上方
            for i in range(1, m):
                grid[i][0] += grid[i - 1][0]
            # 第一行只能来自左边
            for i in range(1, n):
                grid[0][i] += grid[0][i - 1]
            # 遍历后续每一个位置
            for i in range(1, m):
                for j in range(1, n):
                    # 增加来自左边的与上边的之间的较大值
                    grid[i][j] += max(grid[i - 1][j], grid[i][j - 1])
            return grid[m - 1][n - 1]