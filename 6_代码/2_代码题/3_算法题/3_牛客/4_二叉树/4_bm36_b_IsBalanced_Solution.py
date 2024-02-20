
# 描述
# 输入一棵节点数为 n 二叉树，判断该二叉树是否是平衡二叉树。
# 在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
# 平衡二叉树（Balanced Binary Tree），
# 具有以下性质：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，
# 并且左右两个子树都是一棵平衡二叉树。

# 自己
class Solution:
    def IsBalanced_Solution(self, pRoot: TreeNode) -> bool:
        # write code here
        if pRoot == None:
            return True
        # 提前阻断，可行性剪枝
        if not self.IsBalanced_Solution(pRoot.left):
            return False
        if not self.IsBalanced_Solution(pRoot.right):
            return False
        left = self.maxDepth(pRoot.left)
        right = self.maxDepth(pRoot.right)
        if abs(left - right) < 2:
            return True
        else:
            return False

    def maxDepth(self, root: TreeNode) -> int:
        # write code here
        if root == None:
            return 0
        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)
        return max(left, right)



class Solution:
    def high(self, root):
        if root == None:
            return 0
        left = self.high(root.left)
        right = self.high(root.right)
        ans = max(left, right) + 1
        return ans

    def IsBalanced_Solution(self, pRoot):
        if pRoot == None:
            return True
        # 提前阻断，可行性剪枝
        if not self.IsBalanced_Solution(pRoot.left):
            return False
        if not self.IsBalanced_Solution(pRoot.right):
            return False
        highleft = self.high(pRoot.left)
        highright = self.high(pRoot.right)
        isbalance = highleft - highright
        # 当前节点高度差
        if isbalance > 1 or isbalance < -1:
            return False
        return True