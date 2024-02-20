
# leetcode 397. 整数替换

# 给定一个正整数 n ，你可以做如下操作：
#
# 如果 n 是偶数，则用 n / 2替换 n 。
# 如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。
# 返回 n 变为 1 所需的 最小替换次数 。
#
#  
#
# 示例 1：
#
# 输入：n = 8
# 输出：3
# 解释：8 -> 4 -> 2 -> 1

# 示例 2：
#
# 输入：n = 7
# 输出：4
# 解释：7 -> 8 -> 4 -> 2 -> 1
# 或 7 -> 6 -> 3 -> 2 -> 1

print(5//2)
def integerReplacement(self, n: int) -> int:
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + self.integerReplacement(n // 2)
    return 2 + min(self.integerReplacement(n // 2), self.integerReplacement(n // 2 + 1))


