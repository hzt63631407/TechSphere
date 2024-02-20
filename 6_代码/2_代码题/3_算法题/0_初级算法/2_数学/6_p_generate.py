
# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
#
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
#
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


def generate(self, numRows: int) -> List[List[int]]:
    ret = []
    for i in range(numRows):
        row = []
        for j in range(0, i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(ret[i - 1][j] + ret[i - 1][j - 1])
        ret.append(row)
    return ret
