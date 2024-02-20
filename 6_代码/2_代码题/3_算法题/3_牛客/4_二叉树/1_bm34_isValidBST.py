
# 描述
# 给定一个二叉树根节点，请你判断这棵树是不是二叉搜索树。
#
# 二叉搜索树满足每个节点的左子树上的所有节点均严格小于当前节点且右子树上的所有节点均严格大于当前节点。

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 中序遍历满足有序
# //如果当前节点值小于等于前一个，说明不是搜索二叉树

class Solution:
    def isValidBST(self , root: TreeNode) -> bool:
        res=[]
        def zhongxu(root):
            if root is None:
                return None
            zhongxu(root.left)
            res.append(root.val)
            zhongxu(root.right)
        zhongxu(root)
        for i in range(1,len(res)):
            #print(res[i-1])
            if res[i]<res[i-1]:
                return False
        return True
