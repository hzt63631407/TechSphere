
# 描述
# 输入一个长度为n的整型数组array，数组中的一个或连续多个整数组成一个子数组，找到一个具有最大和的连续子数组。
# 1.子数组是连续的，比如[1,3,5,7,9]的子数组有[1,3]，[3,5,7]等等，但是[1,3,7]不是子数组
# 2.如果存在多个最大和的连续子数组，那么返回其中长度最长的，该题数据保证这个最长的只存在一个
# 3.该题定义的子数组的最小长度为1，不存在为空的子数组，即不存在[]是某个数组的子数组
# 4.返回的数组不计入空间复杂度计算

class Solution:
    def FindGreatestSumOfSubArray(self , nums: List[int]) -> List[int]:
            start,end = 0,0
            temp,m = nums[0],nums[0]
            for i in range(len(nums)):
                if temp < 0 :
                    start = i
                    temp = nums[i]
                else:
                    temp += nums[i]
                if temp >= m:
                    m = temp
                    end = i
            if start > end:
                return nums[end:end+1]
            return nums[start:end+1]