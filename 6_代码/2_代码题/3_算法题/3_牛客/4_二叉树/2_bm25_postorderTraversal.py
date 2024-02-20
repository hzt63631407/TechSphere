

# 描述
# 给定一个二叉树，返回他的后序遍历的序列。
#
# 后序遍历是值按照 左节点->右节点->根节点 的顺序的遍历。

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self , root: TreeNode) -> List[int]:
        # write code here
        result = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            inorder(root.right)
            result.append(root.val)
        inorder(root)
        return result