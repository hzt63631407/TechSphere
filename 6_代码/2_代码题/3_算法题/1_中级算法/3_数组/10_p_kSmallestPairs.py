
# leetcode 373

# 给定两个以 升序排列 的整数数组 nums1 和 nums2 , 以及一个整数 k 。
#
# 定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。
#
# 请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。
#
#  
#
# 示例 1:
#
# 输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# 输出: [1,2],[1,4],[1,6]
# 解释: 返回序列中的前 3 对数：
#      [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    d = []
    ans = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            temp = nums1[i] + nums2[j]
            d.append([temp, nums1[i], nums2[j]])
    l = sorted(d, key=lambda x: x[0])
    print(l)
    if len(l) < k:
        k = len(l)
    for i in range(k):
        ans.append([l[i][1], l[i][2]])
    return ans



# 好一点答案     # 超时
def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    t = []
    for i in nums1:
        for j in nums2:
            t.append([i, j])
    t.sort(key = lambda x : x[0] + x[1])
    return t[:k]

