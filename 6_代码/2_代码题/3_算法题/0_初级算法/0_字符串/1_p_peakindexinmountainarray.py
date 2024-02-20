# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 如果以下属性成立，我们将数组A称为山峰：
#
# A.length >= 3
# 存在一些0 < i < A.length - 1这样的A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# 鉴于一个绝对是一座山的阵列，返回任何  i 这样的  A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]。
#
# 例1：
#
# 输入：[0,1,0]
# 输出：1
# 例2：
#
# 输入：[0,2,1,0]
# 输出：1

# 《代码随想录》
# https://programmercarl.com



# 先求出最大值和最大值的坐标
def ismountainarray(s):
    m = max(s)
    a = s.index(m)
    return m,a
#   return arr.index(max(arr))

print(ismountainarray([2,3,4,2,6]))
print(ismountainarray("23245484"))



# 前面理解错误，题目只是让求坐标，所以只是求最大值坐标即可


# 根据最大值，将数组分成两段
# 自己，方法不是很好 答案正常
# def ismountainarray(s):
#     m = max(s)
#     a = s.index(m)
#     for i in range(0,a+1):
#         if s[i] < s[i+1]:
#             continue
#         else:
#             if i != a:                                      # 可能会出现前半段没有循环完就判断下一部分，如果前半端出现了前面的数大于后面的数，就直接返回
#                 return 0
#             for i in range(a+1,len(s)):
#                 if s[i-1] > s[i]:
#                     continue
#                 else:
#                     return 0
#     return 1

# print(ismountainarray([1,3,5,4,2,1]))

