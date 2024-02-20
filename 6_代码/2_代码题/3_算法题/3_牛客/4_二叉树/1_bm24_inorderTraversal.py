
# 描述
# 给定一个二叉树的根节点root，返回它的中序遍历结果。
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self , root: TreeNode) -> List[int]:
        # write code here
        result = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
        inorder(root)
        return result