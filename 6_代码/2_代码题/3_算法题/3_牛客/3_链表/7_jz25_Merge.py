
# 描述
# 输入两个递增的链表，单个链表的长度为n，合并这两个链表并使新链表中的节点仍然是递增排序的。

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#   自己 需要精简
def Merge(self, l1: ListNode, l2: ListNode) -> ListNode:
    # write code here
    res = ListNode(0)
    temp = res
    while l1 and l2:
        if l1.val < l2.val:
            temp.next = l1
            temp = temp.next
            l1 = l1.next
        else:
            temp.next = l2
            temp = temp.next
            l2 = l2.next
    if l1 and not l2:
        temp.next = l1
        temp = temp.next
        l1 = l1.next
    if l2 and not l1:
        temp.next = l2
        temp = temp.next
        l2 = l2.next
    return res.next


class Solution:
    def Merge(self , l1: ListNode, l2: ListNode) -> ListNode:
        # write code here
        res = ListNode(None)          # 不确定那个是头节点，先创建一个哑节点
        node = res
        while l1 and l2:
            if l1.val < l2.val:        # 如果l1小，下一个节点是l1，并且l1向前移
                node.next, l1 = l1, l1.next
            else:
                node.next, l2 = l2, l2.next
            node = node.next
        if l1:                         # 如果只存在l1,链接上即可
            node.next = l1
        else:
            node.next = l2
        return res.next                # 返回哑节点的下一个节点，即节点