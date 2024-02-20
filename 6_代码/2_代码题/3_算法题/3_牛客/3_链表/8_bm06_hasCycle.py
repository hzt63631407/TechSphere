
# 描述
# 判断给定的链表中是否有环。如果有环则返回true，否则返回false。

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 自己
def hasCycle(self, head: ListNode) -> bool:
    fast = head
    slow = head
    while fast:
        if fast.next:
            fast = fast.next.next
        else:
            return False
        slow = slow.next
        if fast == slow:
            return True
    return False


class Solution:
    def hasCycle(self , head):
        # write code here
        if not head:
            return False
        # 双指针  快慢指针
        slow = head
        fast = head
        while slow and fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False
            # 当双指针相遇 即表示指针有环
            if slow == fast:
                return True
        return False
