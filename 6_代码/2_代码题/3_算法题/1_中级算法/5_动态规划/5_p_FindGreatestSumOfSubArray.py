
# JZ85 连续子数组的最大和(二)

# 输入一个长度为n的整型数组array，数组中的一个或连续多个整数组成一个子数组，
# 找到一个具有最大和的连续子数组。
# 1.子数组是连续的，比如[1,3,5,7,9]的子数组有[1,3]，[3,5,7]等等，但是[1,3,7]不是子数组
# 2.如果存在多个最大和的连续子数组，那么返回其中长度最长的，该题数据保证这个最长的只存在一个
# 3.该题定义的子数组的最小长度为1，不存在为空的子数组，即不存在[]是某个数组的子数组
# 4.返回的数组不计入空间复杂度计算


# 自己 数组一直叠加，如果是0，则抛弃前面的数组，重新开始累加
def FindGreatestSumOfSubArray(self , array: List[int]) -> List[int]:
    # write code here
    maxval = array[0]
    temp = array[0]  # 序列累加
    endindex = 0
    beginindex = 0
    for i in range(1, len(array)):
        if temp < 0:
            temp = array[i]
            beginindex = i
        else:
            temp += array[i]
        if temp >= maxval:
            endindex = i
            maxval = temp
    # begin > end 表示 序列全为负
    # begin不断累加， 但此时end已保存最大值索引
    if beginindex > endindex:
        return array[endindex:endindex + 1]
    return array[beginindex:endindex + 1]


# def FindGreatestSumOfSubArray(self , nums: List[int]) -> List[int]:
#     # write code here
#     start,end = 0,1
#     m,t = nums[0],nums[0]
#     for i in range(1,len(nums)):
#         if m < 0:
#             m = nums[i]
#             start = i
#         else:
#             m = m + nums[i]
#         if m >= t:
#             t = m
#             end = i
#     if start>end:
#         return nums[end:end+1]
#     return nums[start:end+1]

