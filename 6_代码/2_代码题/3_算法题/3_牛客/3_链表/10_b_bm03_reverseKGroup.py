

# 描述
# 将给出的链表中的节点每 k 个一组翻转，返回翻转后的链表
# 如果链表中的节点数不是 k 的倍数，将最后剩下的节点保持原样
# 你不能更改节点中的值，只能更改节点本身。

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self , head: ListNode, k: int) -> ListNode:
        # write code here
        tail = head
        #遍历k次到尾部
        for i in range(0,k):
            #如果不足k到了链表尾，直接返回，不翻转
            if tail == None:
                return head
            tail = tail.next
        #翻转时需要的前序和当前节点
        pre = None
        cur = head
        #在到达当前段尾节点前
        while cur != tail:
            #翻转
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        #当前尾指向下一段要翻转的链表
        head.next = self.reverseKGroup(tail, k)
        return pre
