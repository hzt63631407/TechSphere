
# 描述
# 给定一个二叉树，确定他是否是一个完全二叉树。
#
# 完全二叉树的定义：若二叉树的深度为 h，除第 h 层外，
# 其它各层的结点数都达到最大个数，第 h 层所有的叶子结点都连续集中在最左边，
# 这就是完全二叉树。（第 h 层可能包含 [1~2h] 个节点）
#

# 层序遍历
# 实现思路
# 对于完全二叉树，我们关心该树每一层从左到右是否是完全连续的
# 因此层序遍历可以按照层的规则进行遍历
# 在某一层的遍历过程中，如果我们遇到了一个空指针位置，则继续遍历有两种情况
# 如果继续遍历，后面的节点全都是空指针节点，则说明该树是完全二叉树
# 如果继续遍历，后面的节点重新出现了非空节点，则说明该树非完全二叉树

# 层次遍历，如果出现空节点,且后续还出现非空节点的话就不满足完全二叉树定义

class Solution:
    def isCompleteTree(self , root: TreeNode) -> bool:
        # write code here
        if not root:
            return True
        q = [root]
        flag = False
        while q:
            for i in range(len(q)):
                cur = q.pop(0)
                # 第一次碰到空节点，改一下标记
                if not cur:
                    flag = True
                else:                       #非空时，继续访问
                    if flag:
                        return False
                    q.append(cur.left)
                    q.append(cur.right)
        return True
