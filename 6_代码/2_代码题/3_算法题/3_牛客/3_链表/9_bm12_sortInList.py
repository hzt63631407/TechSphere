

# 描述
# 给定一个节点数为n的无序单链表，对其按升序排序。

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortInList(self , head: ListNode) -> ListNode:
        # write code here
        cur = head
        t = []
        while cur:
            t.append(cur.val)
            cur = cur.next
        t.sort()
        res = ListNode(0)
        temp = res
        for i in range(len(t)):
            temp.next = ListNode(t[i])
            temp = temp.next
        return res.next


class Solution:
    def sortInList(self , head: ListNode) -> ListNode:
        # write code here
        cur = head
        t = []
        while cur:
            t.append(cur.val)
            cur = cur.next
        t.sort()
        res = ListNode(t[0])
        temp = res                                  # 把头节点用变量存储，然后放进循环
        for i in range(1,len(t)):
            temp.next = ListNode(t[i])                       # 进行循环
            temp = temp.next
        return res