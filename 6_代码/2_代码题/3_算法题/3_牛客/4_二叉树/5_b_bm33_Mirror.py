


# 描述
# 操作给定的二叉树，将其变换为源二叉树的镜像。

class Solution:
    def Mirror(self , pRoot: TreeNode) -> TreeNode:
        # write code here
        if not pRoot:
            return None
        # 先递归子树     一直执行
        left = self.Mirror(pRoot.left)
        right = self.Mirror(pRoot.right)
        # 交换
        pRoot.left = right
        pRoot.right = left
        return pRoot