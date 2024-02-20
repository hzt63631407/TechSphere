


# 描述
# 给定一棵二叉树(保证非空)以及这棵树上的两个节点对应的val值
# o1 和 o2，请找到 o1 和 o2 的最近公共祖先节点。


class Solution:
    def lowestCommonAncestor(self , root: TreeNode, o1: int, o2: int) -> int:
        if not root:
            return
        if root.val == p or root.val == q:
            return root.val

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        print(root.val, left, right)

        if left != None and right != None: # 小坑! 不能用not left and not right
            return root.val
        if not right:
            return left
        if not left:
            return right