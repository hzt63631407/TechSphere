


# 描述
# 给定一个二叉树，返回该二叉树层序遍历的结果，（从左到右，一层一层地遍历）

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self , root: TreeNode) -> List[List[int]]:
    # write code here
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            length = len(queue)
            level = []
            for i in range(length):
                node = queue.pop(0)                                 # [1]
                level.append(node.val)                              # 先把[1]加进来
                if node.left:                                       # 下次循环，对[2,3]进行循环，level加进来[2]，2循环完成了，,此时queue有[4,5]
                    queue.append(node.left)                         # 因为循环的是len，再对3进行循环，level加进来[3]，3循环完成了，,此时queue有[4,5,6]
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res