# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给你一个链表的头节点 head ，判断链表中是否有环。
#
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
#
# 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
#
# 注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
#
# 如果链表中存在环 ，则返回 true 。 否则，返回 false 。


# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。

# 输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。

# 答案
def hasCycle(self, head: Optional[ListNode]) -> bool:
    l = []
    while head:
        if head in l:
            return True
        l.append(head)
        head = head.next
    return False


# 答案 只有我的代码这么奇葩嘛？
def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    while head:
        if head.val == 'bjfuvth':
            return True
        else:
            head.val = 'bjfuvth'            # 把前面的节点都附值成一个少见的值，然后后面节点去判断，如果有，就有循环。
        head = head.next
    return False


# def hasCycle(self, head: ListNode) -> bool:
#     seen = set()
#     while head:
#         if head in seen:
#             return True
#         seen.add(head)
#         head = head.next
#     return False