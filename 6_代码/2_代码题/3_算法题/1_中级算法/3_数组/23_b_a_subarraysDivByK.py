
# 974. 和可被 K 整除的子数组
#
# 给定一个整数数组 nums 和一个整数 k ，返回其中元素之和可被 k 整除的（连续、非空） 子数组 的数目。
#
# 子数组 是数组的 连续 部分。
#
# 输入：nums = [4,5,0,-2,-3,1], k = 5
# 输出：7
# 解释：
# 有 7 个子数组满足其元素之和可被 k = 5 整除：
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        record = {0: 1}
        total, ans = 0, 0
        for elem in nums:
            total += elem
            modulus = total % k
            same = record.get(modulus, 0)
            ans += same
            record[modulus] = same + 1
        return ans
