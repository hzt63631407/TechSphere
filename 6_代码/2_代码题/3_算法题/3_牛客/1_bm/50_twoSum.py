
# 描述
# 给出一个整型数组 numbers 和一个目标值 target，
# 请在数组中找出两个加起来等于目标值的数的下标，返回的下标按升序排列。
# （注：返回的数组下标从1开始算起，保证target一定可以由数组里面2个数字相加得到）

class Solution:
    def twoSum(self , array: List[int], target: int) -> List[int]:
        # write code here
            res = []
            d = {}
            for i in range(len(array)):
                t = target - array[i]
                if t not in d:
                    d[array[i]] = i
                else:
                    res.append(d[t]+1)
                    res.append(i+1)
                    break
            return res