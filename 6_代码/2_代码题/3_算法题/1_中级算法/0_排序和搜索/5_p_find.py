# 描述

# 在一个二维数组array中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
# [
# [1,2,8,9],
# [2,4,9,12],
# [4,7,10,13],
# [6,8,11,15]
# ]
# 给定 target = 7，返回 true。
# 给定 target = 3，返回 false。

# 从左下角元素往上查找，右边元素是比这个元素大，上边是的元素比这个元素小。
# 于是，target比这个元素小就往上找，比这个元素大就往右找。
# 如果出了边界，则说明二维数组中不存在target元素。

def Find(self, target, array):
    # write code here
    rows = len(array) - 1
    cols = len(array[0]) - 1
    i = rows
    j = 0
    while j<= cols and i >= 0:
        if target < array[i][j]:
            i -= 1
        elif target > array[i][j]:
            j += 1
        else:
            return True
    return False
