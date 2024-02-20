# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，
#
# 并以列表形式返回。你可以按 任意顺序 返回这些组合。
#
# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
#
# 对于给定的输入，保证和为 target 的不同组合数少于 150 个。

# 输入: candidates = [2,3,5], target = 8
# 输出: [[2,2,2,2],[2,3,3],[3,5]]

# https://leetcode-cn.com/problems/combination-sum/comments/

# 答案  暂时理解不了 先背答案
def combinationSum(self, candidates: list, target: int):
    candidates.sort()
    n = len(candidates)
    res = []
    def backtrack(i, tmp_sum, tmp):
        if tmp_sum > target or i == n:
            return
        if tmp_sum == target:
            res.append(tmp)
            return
        for j in range(i, n):
            if tmp_sum + candidates[j] > target:
                break
            backtrack(j, tmp_sum + candidates[j], tmp + [candidates[j]])

    backtrack(0, 0, [])
    return res

