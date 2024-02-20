# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 输入一个长度为 n 的链表，设链表中的元素的值为 ai ，返回该链表中倒数第k个节点。
# 如果该链表长度小于k，请返回一个长度为 0 的链表。

def FindKthToTail(self , pHead: ListNode, k: int) -> ListNode:
    # write code here
    fast = pHead
    slow = pHead
    # 快指针先走k步
    for i in range(0, k):
        if not fast:
            return None
        fast = fast.next
    # 双指针同时行走
    while fast:
        fast = fast.next
        slow = slow.next
    return slow

# 如果返回的是头节点
# def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#     # write code here
#     if not head:
#         return None
#     # 定义快慢指针
#     slow = head
#     fast = head
#     for i in range(n):
#         fast = fast.next
#     # 判断n是否大于head的长度
#     if not fast:
#         return head.next
#     # 快慢指针同时行走
#     while fast.next:
#         fast = fast.next
#         slow = slow.next
#     # 删除结点
#     slow.next = slow.next.next
#     return head
