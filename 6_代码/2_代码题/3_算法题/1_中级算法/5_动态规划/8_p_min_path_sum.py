# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

#
# 给定一个包含非负整数的 m x n 网格 grid ，
# 请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
#  
#
# 示例 1：
#
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
#
#
# 示例 2：
#
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
# https://leetcode-cn.com/problems/minimum-path-sum/
# https://leetcode-cn.com/problems/minimum-path-sum/solution/zui-xiao-lu-jing-he-dong-tai-gui-hua-gui-fan-liu-c/https://leetcode-cn.com/problems/minimum-path-sum/solution/zui-xiao-lu-jing-he-dong-tai-gui-hua-gui-fan-liu-c/


class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]            # 从左边和右边取最小值 加上本身
        return grid[-1][-1]

