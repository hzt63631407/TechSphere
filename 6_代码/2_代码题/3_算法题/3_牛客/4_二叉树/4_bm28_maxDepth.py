
# 描述
# 求给定二叉树的最大深度，
# 深度是指树的根节点到任一叶子节点路径上节点的数量。
# 最大深度是所有叶子节点的深度的最大值。

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self , root: TreeNode) -> int:
        # write code here
        if not root:
            return 0
        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)
        return max(left,right)