
# 描述
# 给定一个单链表的头结点pHead(该头节点是有值的，比如在下图，它的val是1)，
# 长度为n，反转该链表后，返回新链表的表头

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 5不太熟悉

class Solution:
    def ReverseList(self , head: ListNode) -> ListNode:
        # write code here
        current = head              # 当前节点
        pre = None                  # 前节点
        temp = None                 # 下一个节点
        while current:
            temp = current.next        # 存储下一个节点
            current.next = pre         # 进行反转

            # 向前一个节点
            pre = current               # 当前给再前
            current = temp              # 后面给当前
        return pre