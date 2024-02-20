

# 描述
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
# 1.对于该题的最近的公共祖先定义:对于有根树T的两个节点p、q，
# 最近公共祖先LCA(T,p,q)表示一个节点x，
# 满足x是p和q的祖先且x的深度尽可能大。在这里，一个节点也可以是它自己的祖先.
# 2.二叉搜索树是若它的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
# 若它的右子树不空，则右子树上所有节点的值均大于它的根节点的值
# 3.所有节点的值都是唯一的。
# 4.p、q 为不同节点且均存在于给定的二叉搜索树中。

# 1.如果pq有一个等于根节点，那么就是根节点
# 2.如果不相等，那么求出他们是否在左右子树
# 3.如果左右子树都有值，那么就是根节点
# 4.如果一颗树没有值，那么就是另一颗树的节点

# 1.同时传入根节点，左节点，右节点self.lowestCommonAncestor(root.left, p, q)
# 2.如果都有节点都不是空，就是根节点，如果一方是空，那就是另一个

class Solution:
    def lowestCommonAncestor(self , root: TreeNode, p: int, q: int) -> int:
        if not root:
            return
        if root.val == p or root.val == q:
            return root.val

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        print(root.val, left, right)

        if left != None and right != None:      # 小坑! 不能用left and right   因为left或者right可能是0
            return root.val
        if not right:
            return left
        if not left:
            return right