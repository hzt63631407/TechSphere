
# 229. 多数元素 II

# 给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

# 输入：nums = [3,2,3]
# 输出：[3]

# def majorityElement(self, nums: List[int]) -> List[int]:
#     l = len(nums) // 3
#     d = {}
#     a = []
#     for i in range(len(nums)):
#         if nums[i] not in d:
#             d[nums[i]] = 1
#         else:
#             d[nums[i]] += 1
#     li = sorted(d.items(), key=lambda x: x[1], reverse=True)
#     # print(li)
#     for i in range(len(li)):
#         print(li[i][1])
#         if li[i][1] > l:
#             a.append(li[i][0])
#     return a
