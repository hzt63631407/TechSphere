# 1.leetcode46 全排列
# 给定一个没有重复数字的序列，返回其所有可能的全排列
# 示例：
# 输入：[1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
# def backtrack(nums,track):
#
#     #路径结束满足约束条件
#     if not nums:
#         results.append(track)
#         return
#
#     #更新选择列表和路径，递归
#     #在这个问题中，选择有 n-len(track)这么多种
#     for i in range(len(nums))：
#         backtrack(nums[:i]+nums[i+1:],track+[nums[i]])
#
# backtrack(nums,[])
# return results


list1 = ['physics', 'chemistry', 1997, 2000]
print("list1[:1]",list1[:1])                # 获取第一个元素
print("list1[1:]",list1[1:])                # 获取除第一个元素外的所有元素


def permute(nums):
    result = []
    def backtrack(nums, track):

        if not nums:
            result.append(track)
            return

        for i in range(len(nums)):
            backtrack(nums[:i] + nums[i + 1:], track + [nums[i]])      # nums_all[:i] + nums_all[i + 1:] 相当于remove了[i]
                    # [2,3][1]
                    # [3][1,2]
                    # [2][1,3]
                    # [1,3][2]
                    # [3][2,1]
                    # [1][2,3]
        # nums[:i] + nums[i + 1:]
        # 每次remove掉list的第i个元素

# nums = [1,2,3]
# permute(nums)

