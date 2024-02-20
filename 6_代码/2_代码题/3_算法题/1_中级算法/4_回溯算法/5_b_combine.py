

# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
#
# 你可以按 任何顺序 返回答案。

# 输入：n = 4, k = 2
# 输出：
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]


def combine(self, n: int, k: int) -> List[List[int]]:
    res = []
    path = []
    def backtrack(n, k, StartIndex):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(StartIndex, n- (k - len(path)) + 2):
            path.append(i)
            backtrack(n, k, i + 1)
            path.pop()

    backtrack(n, k, 1)
    return res