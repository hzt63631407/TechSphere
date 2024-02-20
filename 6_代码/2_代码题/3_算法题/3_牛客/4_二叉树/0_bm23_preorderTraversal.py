
# 描述
# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 26,34,36 不熟

# 31,33 nc315 ok

class Solution:
    def preorderTraversal(self , root: TreeNode) -> List[int]:
        # write code here
        result = []
        def inorder(root):
            if not root:
                return
            result.append(root.val)
            inorder(root.left)
            inorder(root.right)
        inorder(root)
        return result