
# 描述
# 给定一个链表，删除链表的倒数第 n 个节点并返回链表的头指针.

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self , head: ListNode, n: int) -> ListNode:
        # write code here
        if not head:
            return None
        # 定义快慢指针
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        # 判断n是否大于head的长度
        if not fast:                                    # 因为n一定有效，所以判断可以写在循环外面
            return head.next                            # 因为head被删除了，所以返回了head.next
        # 快慢指针同时行走
        while fast.next:                                # 如果需要next.next 那么循环用next
            fast = fast.next
            slow = slow.next
        # 删除结点
        slow.next = slow.next.next
        return head
