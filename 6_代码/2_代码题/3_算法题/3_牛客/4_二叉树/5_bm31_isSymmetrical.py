

# 描述
# 给定一棵二叉树，判断其是否是自身的镜像（即：是否对称）

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetrical(self, pRoot: TreeNode) -> bool:
        # write code here
        if pRoot == None:
            return True
        else:
            return self.compare(pRoot.left, pRoot.right)

    # 左的左和右的右对比
    def compare(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        elif left.val != right.val:
            return False
        else:
            return self.compare(left.right, right.left) and self.compare(left.left, right.right)
