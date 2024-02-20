
# 描述
# 删除给出链表中的重复元素（链表中元素从小到大有序），使链表中的所有元素都只出现一次

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self , head: ListNode) -> ListNode:
        # write code here
        if head == None:
            return None
        #遍历指针
        cur = head
        #指针当前和下一位不为空
        while cur.next:                         #  如果需要next.next 那么循环用next
            #如果当前与下一位相等则忽略下一位
            if(cur.val == cur.next.val):        # 删除重复的节点不用保存前节点 用cur cur.next cur.next.next
                cur.next = cur.next.next
            #否则指针正常遍历
            else:
                cur = cur.next
        return head
