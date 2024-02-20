


# 已知两颗二叉树，将它们合并成一颗二叉树。
# 合并规则是：都存在的结点，就将结点值加起来，否则空的位置就由另一个树的结点来代替。

class Solution:
    def mergeTrees(self , t1: TreeNode, t2: TreeNode) -> TreeNode:
        # 若只有一个节点返回另一个，两个都为NULL自然返回NULL
        if not t1:
            return t2
        if not t2:
            return t1
        # 根左右的方式递归
        head = TreeNode(t1.val + t2.val)
        head.left = self.mergeTrees(t1.left, t2.left)
        head.right = self.mergeTrees(t1.right, t2.right)
        return head