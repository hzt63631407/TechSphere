
# 描述
# 输入一个长度为 n 的链表，设链表中的元素的值为 ai ，返回该链表中倒数第k个节点。
# 如果该链表长度小于k，请返回一个长度为 0 的链表。

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self , pHead: ListNode, k: int) -> ListNode:
        # write code here
        slow = pHead
        fast = pHead
        for i in range(k):
            if not fast:
                return None
            fast = fast.next
        while fast:                        # 需要fast走到头，所以用fast，即使下个next=none也可以
            fast = fast.next
            slow  = slow.next
        return slow