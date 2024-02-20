

# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
#
# 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
#
# 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
#
# 不允许修改 链表。

# 一个非常直观的思路是：我们遍历链表中的每个节点，并将它记录下来；
# 一旦遇到了此前遍历过的节点，就可以判定链表中存在环。

# 自己 先用这个答案
# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         dir = []
#         while head != None and head.next != None:
#             if head.val not in dir:
#                 dir.append(head.val)
#             if head.next.val in dir:
#                 return head.next
#             else:
#                 head = head.next
#         return None


# 双指针思路 # 暂时不理解 背答案
# https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/
# class Solution(object):
#     def detectCycle(self, head):
#         fast, slow = head, head
#         while True:
#             if not (fast and fast.next): return
#             fast, slow = fast.next.next, slow.next
#             if fast == slow: break
#         fast = head
#         while fast != slow:
#             fast, slow = fast.next, slow.next
#         return fast


# 第一种结果： fast 指针走过链表末端，说明链表无环，直接返回

# 第二种结果
# 设链表共有 a+b 个节点
# 走a+nb步一定是在环入口
# 第一次相遇时慢指针已经走了nb步
