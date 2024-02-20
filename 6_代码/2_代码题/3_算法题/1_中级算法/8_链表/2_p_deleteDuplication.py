# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
# 例如，链表 1->2->3->3->4->4->5  处理后为 1->2->5

# 输入：
# {1,2,3,3,4,4,5}
# 返回值：
# {1,2,5}

# 答案 都删除
# def deleteDuplication(self, pHead: ListNode) -> ListNode:
#     # 空链表
#     if pHead == None:
#         return None
#     res = ListNode(0)
#     # 在链表前加一个表头
#     res.next = pHead
#     cur = res
#     while cur.next and cur.next.next:
#         # 遇到相邻两个节点值相同
#         if cur.next.val == cur.next.next.val:
#             temp = cur.next.val
#             # 将所有相同的都跳过
#             while cur.next != None and cur.next.val == temp:
#                 cur.next = cur.next.next
#         else:
#             cur = cur.next
#     # 返回时去掉表头
#     return res.next


# 答案 还保留一个
# def deleteDuplication(self, pHead: ListNode) -> ListNode:
#     if head == None:
#         return None
#     # 遍历指针
#     cur = head
#     # 指针当前和下一位不为空
#     while cur and cur.next:
#         # 如果当前与下一位相等则忽略下一位
#         if (cur.val == cur.next.val):
#             cur.next = cur.next.next
#         # 否则指针正常遍历
#         else:
#             cur = cur.next
#     return head

#
