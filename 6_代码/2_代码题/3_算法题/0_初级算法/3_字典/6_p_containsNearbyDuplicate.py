# leetcode 219. 存在重复元素 II
#
# 给你一个整数数组 nums 和一个整数 k ，
# 判断数组中是否存在两个 不同的索引 i 和 j ，
# 满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。


# 从左到右遍历数组 \textit{nums}nums，当遍历到下标 ii 时，如果存在下标 j < i,
# 使得nums[i]=nums[j]，则当i−j≤k 时即找到了两个符合要求的下标 j和 i。


# 答案
def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    d = {}
    for i in range(len(nums)):
        if nums[i] in d and abs(d[nums[i]] - i) <= k:
            return True
        else:
            d[nums[i]] = i
    return False


# 第二种答案
def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    d = {}
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = i
        else:
            if i - d[nums[i]] <= k:
                return True
            else:
                d[nums[i]] = i
    return False



# 自己 没有进行更新
# def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#     l = []
#     for i in range(len(nums)):
#         if nums[i] not in l:
#             l.append(nums[i])
#         else:
#             j = l.index(nums[i])
#             if abs(i - j) <= k:
#                 return True
#     return False