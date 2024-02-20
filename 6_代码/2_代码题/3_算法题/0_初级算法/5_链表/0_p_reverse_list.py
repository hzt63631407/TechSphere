# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
#
# 示例:
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
# 进阶:
# 你可以迭代F或递归地反转链表。你能否用两种方法解决这道题？


# 例子
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

e4 = Node('4')
e5 = Node('5')
e1 = Node('1')
e9 = Node('9')

e4.next = e5                     # 对象的一个属性是下一个对象
e5.next = e1
e1.next = e9


# e4有两个属性
# e4.val = 4
# e4.next = 5
# 反转就是e5.next = 4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        current = head              # 当前节点
        pre = None                  # 前节点
        next = None                 # 下一个节点
        while current:
            next = current.next        # 存储下一个节点
            current.next = pre         # 进行反转

            # 向前一个节点
            pre = current               # 当前给再前
            current = next              # 后面给当前
        return pre

# 答案
# 步骤思路：
#  //1. temp  保存临时变量
#  //2. change 改变链表
#  //3. next   迭代当前指向
# class Solution {
#     public ListNode reverseList(ListNode head) {
#         ListNode pev = null;
#         ListNode cur = head;
#         while(cur!=null){
#             //1. temp  保存临时变量
#             ListNode next = cur.next;
#             //2. change 改变链表
#             cur.next = pev;
#             //3. next   迭代当前指向
#             pev = cur;
#             cur = next;
#         }
#         return pev;
#     }
# }

# 以前
# class Solution:
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         p, rev = head, None
#         while p:
#             rev, rev.next, p = p, rev, p.next
#         return rev

# ListNode prev = null; //前指针节点
# ListNode curr = head; //当前指针节点
# //每次循环，都将当前节点指向它前面的节点，然后当前节点和前节点后移
# while (curr != null) {
#     ListNode nextTemp = curr.next; //临时节点，暂存当前节点的下一节点，用于后移
#     curr.next = prev; //将当前节点指向它前面的节点
#     prev = curr; //前指针后移
#     curr = nextTemp; //当前指针后移

if __name__ == "__main__":
    s = Solution()
    print(s.reverseList(e4))
    # print(e4.next.val)
    print(e5.next.val)
    print(e1.next.val)
    print(e9.next.val)

