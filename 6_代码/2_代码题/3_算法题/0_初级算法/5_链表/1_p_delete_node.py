# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 请编写一个函数，用于 删除单链表中某个特定节点 。在设计函数时需要注意，你无法访问链表的头节点 head ，只能直接访问 要被删除的节点 。
#
# 题目数据保证需要删除的节点 不是末尾节点 。
#
# 现有一个链表 -- head = [4,5,1,9]，它可以表示为:

# 输入: head = [4, 5, 1, 9], node = 5
# 输出: [4, 1, 9]
# 解释: 给定你链表中值为
# 5
# 的第二个节点，那么在调用了你的函数之后，该链表应变为
# 4 -> 1 -> 9.
# 示例
# 2:
#
# 输入: head = [4, 5, 1, 9], node = 1
# 输出: [4, 5, 9]
# 解释: 给定你链表中值为
# 1
# 的第三个节点，那么在调用了你的函数之后，该链表应变为
# 4 -> 5 -> 9.
#
# 说明:
#
# 链表至少包含两个节点。
# 链表中所有节点的值都是唯一的。
# 给定的节点为非末尾节点并且一定是链表中的一个有效节点。
# 不要从你的函数中返回任何结果。


class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

e4 = Node('4')
e5 = Node('5')
e1 = Node('1')
e9 = Node('9')

e4.next = e5                     # 对象的一个属性是下一个对象
e5.next = e1
e1.next = e9


# print(e4.nextval.dataval)       # 5
# print(e5.nextval.dataval)       # 1
# print(e1.nextval.dataval)       # 9
# print(e9.nextval.dataval)


# 答案
def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next

# 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。返回删除后的链表的头节点。
# 1.此题对比原题有改动
# 2.题目保证链表中节点的值互不相同
# 3.该题只会输出返回的链表和结果做对比，所以若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点
# def deleteNode(self, head: ListNode, val: int) -> ListNode:
#     # 加入一个头节点
#     res = ListNode(0)
#     res.next = head
#     # 前序节点
#     pre = res
#     # 当前节点
#     cur = head
#     # 遍历链表
#     while cur is not None:
#         # 找到目标节点
#         if cur.val == val:
#             # 断开连接
#             pre.next = cur.next
#             break
#         pre = cur
#         cur = cur.next
#     # 返回去掉头节点
#     return res.next
#


# 官方
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# def deleteNode(node):
#     """
#     :type node: ListNode
#     :rtype: void Do not return anything, modify node in-place instead.
#     """
#     node.dataval, node.nextval = node.nextval.dataval, node.nextval.nextval

# [4,5,1,9]
if __name__ == "__main__":
    print(delete_node(e5))
    print(e4.next.val)
    print(e5.next.val)
    print(e1.next.val)
