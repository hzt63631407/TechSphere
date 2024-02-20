# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


e1 = Node(1)
e2 = Node(2)
e4 = Node(4)

e1.next = e2  # 对象的一个属性是下一个对象
e2.next = e4


d1 = Node(1)
d3 = Node(3)
d4 = Node(4)
# d5 = Node(5)


d1.next = d3  # 对象的一个属性是下一个对象
d3.next = d4
# d4.nextval = d5

# 答案
# def mergeTwoLists(self, l1, l2):
#     """
#     :type list1: Optional[ListNode]
#     :type list2: Optional[ListNode]
#     :rtype: Optional[ListNode]
#     """
#     res = ListNode(None)                              # 不确定那个是头节点，先创建一个哑节点
#     node = res
#     while l1 and l2:
#         if l1.val < l2.val:                           # 如果l1小，下一个节点是l1，并且l1向前移
#             node.next, l1 = l1, l1.next
#         else:
#             node.next, l2 = l2, l2.next
#         node = node.next
#     if l1:                                            # 如果只存在l1,链接上即可
#         node.next = l1
#     else:
#         node.next = l2
#     return res.next                                   # 返回哑节点的下一个节点，即节点


# if __name__ == "__main__":
    # print(mergetwolists(d1, e1))
    # print()
    # print(d1.next.val)
    # print(e1.next.val)
    # print(e2.next.val)
    # print(d4.nextval.dataval)
    # print(e4.next.val)


#   e1.ne = me(d1,e2)   e1.ne = d1
#    re e1
#   d1.ne = me(d3,e2)
#    re d1
#   e2.ne = me(d3,e4)
#    re e2
#   d3.ne = me(d4,e4)
#    re d3
#   e3.ne = me(d4,None)
#    re e4
#
