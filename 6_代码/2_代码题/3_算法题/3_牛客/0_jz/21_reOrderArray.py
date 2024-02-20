
# 描述
# 输入一个长度为 n 整数数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有的奇数位于数组的前面部分，所有的偶数位于数组的后面部分，
# 并保证奇数和奇数，偶数和偶数之间的相对位置不变。


class Solution:
    def reOrderArray(self , array: List[int]) -> List[int]:
        # write code here
        # write code here
        array.sort(key=self.rule)
        return array
    def rule(self,m):
        if  m % 2 == 0:
            return 1
        else:
            return 0