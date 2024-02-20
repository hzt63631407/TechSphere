
# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

# 思路
# 先遍历第一个链表到他的尾部
# 然后将尾部的next指针指向第二个链表(尾部指针的next本来指向的是null)。
# 这样两个链表就合成了一个链表，判断原来的两个链表是否相交也就转变成了判断新的链表是否有环的问题了：即判断单链表是否有环？

# 答案
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    l1 = headA  # 题目要求链表必须保持其原始结构，所以分别用新的指针指向链表的头节点
    l2 = headB
    while l1 != l2:
        if l1 == None:
            l1 = headB
        else:
            l1 = l1.next  # 如果l1为空，就将l1指向headB
        if l2 == None:
            l2 = headA
        else:
            l2 = l2.next
    return l1

# 自己思考
# if l1 == None: 和 l2 == None: 同时走
# l1过程[4，1，8，4，5，5，6，1，8]
# l2过程[5，6，1，8，4，5，5，1，8]
# 在8时 相等，所以返回l1


# def FindFirstCommonNode(self, pHead1, pHead2):
#     # write code here
#     a = pHead1
#     b = pHead2
#     # 当两者相同则是第一个公共节点
#     while a != b:                             # 条件是是否相等
#         # a从pHead1遍历完再遍历pHead2
#         if a:                                 # 不能用a.next 因为是找出
#             a = a.next
#         else:
#             a = pHead2                         # 不能接b，会无限循环。
#         if b:F
#             b = b.next
#         else:
#             b = pHead1
#     return a


