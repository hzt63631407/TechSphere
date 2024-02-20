
# 描述
# 输入两个无环的单向链表，找出它们的第一个公共结点，
# 如果没有公共节点则返回空。
# （注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 123 45       走了123456745
# 67 45        走674512345

class Solution:
    def FindFirstCommonNode(self , headA , headB ):
        # write code here
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