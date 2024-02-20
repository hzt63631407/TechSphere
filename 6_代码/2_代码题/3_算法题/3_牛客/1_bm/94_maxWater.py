

# BM94

# 给定一个整形数组arr，已知其中所有的值都是非负的，将这个数组看作一个柱子高度图，
# 计算按此排列的柱子，下雨之后能接多少雨水。(数组以外的区域高度视为0)

# 这道题也是类似，我们可以将整个图看成一个水桶，两边就是水桶的板，
# 中间比较低的部分就是水桶的底，由较短的边控制水桶的最高水量。
# 但是水桶中可能出现更高的边，比如上图第四列，它比水桶边还要高，
# 那这种情况下它是不是将一个水桶分割成了两个水桶，而中间的那条边就是两个水桶的边。

# 自己整理
# 左边和右边分别是通边，指针往中间遍历，三条边。
# 如果中间遍历时，有更高，就更新这条边的值。
# 用左右两边最低的去中间的边的值，想减能够等到这一列的水量。

class Solution:
    def maxWater(self , arr: List[int]) -> int:
        res = 0
        #左右双指针
        left = 0
        right = len(arr) - 1
        #中间区域的边界高度
        maxL = 0
        maxR = 0
        #直到左右指针相遇
        while left < right:
            #每次维护往中间的最大边界
            maxL = max(maxL, arr[left])
            maxR = max(maxR, arr[right])
            #较短的边界确定该格子的水量
            if maxR > maxL:
                res += maxL - arr[left]
                left += 1
            else:
                res += maxR - arr[right]
                right -= 1
        return res