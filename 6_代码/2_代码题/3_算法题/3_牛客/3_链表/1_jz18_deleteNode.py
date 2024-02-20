
# 描述
# 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。返回删除后的链表的头节点。
#
# 1.此题对比原题有改动
# 2.题目保证链表中节点的值互不相同
# 3.该题只会输出返回的链表和结果做对比，
# 所以若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self , head: ListNode, val: int) -> ListNode:
        # write code here
        res = ListNode(0)
        res.next = head
        # 前序节点
        pre = res
        # 当前节点
        cur = head
        # 遍历链表
        while cur:
            # 找到目标节点
            if cur.val == val:
                # 断开连接
                pre.next = cur.next
                break
            pre = cur                               # 如果需要知道前节点，就需要pre，所以pre也需要向前
            cur = cur.next
        # 返回去掉头节点
        return res.next