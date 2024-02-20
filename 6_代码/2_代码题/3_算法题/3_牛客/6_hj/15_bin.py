
# 输入一个 int 型的正整数，计算出该 int 型数据在内存中存储时 1 的个数。
#
# 数据范围：保证在 32 位整型数字范围内


n = int(input())
n = bin(n)
print(n.count('1'))

