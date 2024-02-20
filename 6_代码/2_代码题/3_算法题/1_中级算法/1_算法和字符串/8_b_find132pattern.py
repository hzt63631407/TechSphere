

# leetcode 456. 132 模式

# 给你一个整数数组 nums ，数组中共有 n 个整数。
#
# 132 模式的子序列 由三个整数 nums[i]、nums[j] 和 nums[k] 组成，
#
# 并同时满足：i < j < k 和 nums[i] < nums[k] < nums[j] 。
#
# 如果 nums 中存在 132 模式的子序列 ，返回 true ；否则，返回 false 。
#
# 示例 1：
#
# 输入：nums = [1,2,3,4]
# 输出：false
# 解释：序列中不存在 132 模式的子序列。

# 使用一个数组来记录：对于下标 i ，那么 min[i] 表示的是从 0 到 i 最小的数是多少。
# 再来一个栈，从后往前遍历原数组，该栈维护的是大于 min[i] 且小于 nums[i] 的元素。

# 假设当前元素 nums[J],要找在 J 之后比 nums[J] 小的数 nums[K],和在 J 之前比 nums[K] 小的数 nums[I],
# 我们可以建立栈从后往前存储数组的元素（或下标），在栈中找nums[K]，
# 再继续向前扫描找 nums[I]。栈中要能够保存比nums[J]下标更大并且值更小的元素，联想到去维护一个单调栈.
# 可以这样去模拟过程：
# 从后往前扫描的过程中，一旦当前元素 nums[I] 比栈顶大，
# 这个 nums[I] 或许就是我们要找的 nums[J]，弹出栈中所有的比它小的元素，
# 这些元素就是符合条件的 nums[K],最后一个弹出的就是符合条件的最大 nums[K],
# 如果这个 num[K] 比继续往前扫描到的 nums[I] 要大，则符合条件。

# 只能用单调栈，不能用递增
def find132pattern(self, nums: List[int]) -> bool:
    stack = []
    num = float('-inf')
    for n in nums[::-1]:
        if n < num:
            return True
        while stack and stack[-1] < n:       # [3,1,4,2] 先添加2，但是2比4小，所以2出来了，如果有一个值小于2，那么就是存在
            num = stack.pop()
        stack.append(n)
    return False

